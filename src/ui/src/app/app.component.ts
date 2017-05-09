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
        svdResults: this.searchResultService.getSearchResults(query, true),
        vsmResults: this.searchResultService.getSearchResults(query, false)
      }).then((data: any) => {
          this.results = <ExtendedSearchResult[]> _.shuffle(_.unionBy(data.svdResults, data.vsmResults, 'doc'))
          this.svdResults = data.svdResults
          this.vsmResults = data.vsmResults
        })
    }
  }

  updateDocument(documentPath: string): void {
    this.documentService.getDocument(documentPath)
      .then(document => this.document = document)
      .catch(() => {})
  }

  calculatePrecision(event, result): void {
    result.relevant = event
    const numberOfRelevantDocs = Math.min(10, _.countBy(this.results, 'relevant')['true'])
    const relevantDocs = _.groupBy(this.results, 'relevant')['true']
    let svdSum = 0
    let svdFoundCounter = 0
    let vsmSum = 0
    let vsmFoundCounter = 0
    for(let i = 0; i < numberOfRelevantDocs; i++) {
      if (_.includes(relevantDocs, this.svdResults[i])) {
        svdFoundCounter += 1
        svdSum += svdFoundCounter / (i + 1)
      }
      if (_.includes(relevantDocs, this.vsmResults[i])) {
        vsmFoundCounter += 1
        vsmSum += vsmFoundCounter / (i + 1)
      }
    }
    if (numberOfRelevantDocs === 0 || numberOfRelevantDocs === NaN) {
      this.svdRPrecision = 0
      this.vsmRPrecision = 0
      this.svdAvgPrecision = 0
      this.vsmAvgPrecision = 0
    } else {
      this.svdAvgPrecision = parseFloat((svdSum / numberOfRelevantDocs).toFixed(3))
      this.vsmAvgPrecision = parseFloat((vsmSum / numberOfRelevantDocs).toFixed(3))
      this.svdRPrecision = parseFloat((svdFoundCounter / numberOfRelevantDocs).toFixed(3))
      this.vsmRPrecision = parseFloat((vsmFoundCounter / numberOfRelevantDocs).toFixed(3))
    }
  } 
}
