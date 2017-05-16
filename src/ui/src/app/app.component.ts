import { Component } from '@angular/core'
import * as P from 'bluebird'
import * as _ from 'lodash'

import { SearchResult } from './search-result'
import { SearchResultsService } from './search-results.service'
import { DocumentService } from './document.service'

class ExtendedSearchResult extends SearchResult {
  relevant: boolean = false
}

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  private title = 'Latent Semantic Indexing Search'
  private query: string = null
  private results: ExtendedSearchResult[] = null
  private allSVDResults: string[] = null
  private allVSMResults: string[] = null
  private selected: string = null
  private document: string = ''
  private useSVD: boolean = true

  private evaluationMode = false
  private svdResults: SearchResult[] = null
  private vsmResults: SearchResult[] = null
  private svdRPrecision: number = 0
  private vsmRPrecision: number = 0
  private svdAvgPrecision: number = 0
  private vsmAvgPrecision: number = 0

  constructor(
    private searchResultService: SearchResultsService,
    private documentService: DocumentService
  ) { }

  updateSearchResults(query: string): void {
    if (!this.evaluationMode) {
      this.searchResultService.getSearchResults(query, this.useSVD)
        .then(searchResults => this.results = <ExtendedSearchResult[]> searchResults)
        .catch(() => {}) // nice error handling tho
    } else {
      P.props({
        svdResults: this.searchResultService.getSearchResults(query, true, 11000),
        vsmResults: this.searchResultService.getSearchResults(query, false, 11000)
      }).then((data: any) => {
          this.allSVDResults = _.map(data.svdResults, ({ doc }) => doc)
          this.allVSMResults = _.map(data.vsmResults, ({ doc }) => doc)
          this.results = <ExtendedSearchResult[]> _.shuffle(_.unionBy(_.slice(data.svdResults, 0, 10), _.slice(data.vsmResults, 0, 10), 'doc'))
          this.svdResults = data.svdResults
          this.vsmResults = data.vsmResults
        })
    }
  }

  updateDocument(documentPath: string): void {
    this.selected = documentPath
    this.documentService.getDocument(documentPath)
      .then(document => this.document = document)
      .catch(() => {})
  }

  calculatePrecision(event: boolean, result: ExtendedSearchResult, query: string): void {
    result.relevant = event
    const relevantDocuments = _.chain(this.results)
      .groupBy('relevant')
      .filter((val, key) => key === 'true')
      .flatten()
      .map(({ doc }) => doc)
      .value()

    const rankedDocumentsSVD = this.allSVDResults
    const rankedDocumentsVSM = this.allVSMResults

    const svdAvgPrecision = this.calculateAvgPrecision(rankedDocumentsSVD, relevantDocuments)
    const vsmAvgPrecision = this.calculateAvgPrecision(rankedDocumentsVSM, relevantDocuments)
    const svdRPrecision = this.calculateRPrecision(rankedDocumentsSVD, relevantDocuments)
    const vsmRPrecision = this.calculateRPrecision(rankedDocumentsVSM, relevantDocuments)

    this.svdAvgPrecision = parseFloat(svdAvgPrecision.toFixed(3))
    this.vsmAvgPrecision = parseFloat(vsmAvgPrecision.toFixed(3))
    this.svdRPrecision = parseFloat(svdRPrecision.toFixed(3))
    this.vsmRPrecision = parseFloat(vsmRPrecision.toFixed(3))
  }

  private calculateAvgPrecision(rankedDocuments: string[], relevantDocuments: string[]): number {    
    const sumOfPrecisions = _.chain(rankedDocuments)
     .map((doc, rank) => ({ doc, rank: rank + 1}))
     .filter(({ doc }) => _.includes(relevantDocuments, doc))
     .map(({ rank }, index) => ( (index + 1) / rank ))
     .tap((array) => {
        if(array.length !== relevantDocuments.length) {
          console.log(`Only found ${array.length} relevant documents. Expected ${relevantDocuments.length}.`)
        }
     })
     .sum()
     .value()

    const precision = sumOfPrecisions / relevantDocuments.length
    return precision
  }

  private calculateRPrecision(rankedDocuments: string[], relevantDocuments: string[]): number {
    if (relevantDocuments.length > rankedDocuments.length) return null

    const slicedRankedDocuments = _.slice(rankedDocuments, 0, relevantDocuments.length)
    const countTruePositives = _.sumBy(slicedRankedDocuments, doc => _.includes(relevantDocuments, doc))

    const precision = countTruePositives / relevantDocuments.length
    return precision
  }

}
