import { Component } from '@angular/core'

import { SearchResult } from './search-result'
import { SearchResultsService } from './search-results.service'
import { DocumentService } from './document.service'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  private title = 'Latent Semantic Indexing Search'
  private query: string = null
  private results: SearchResult[] = null
  private document: string = ''
  private useSVD: boolean = true

  constructor(
    private searchResultService: SearchResultsService,
    private documentService: DocumentService
  ) { }

  updateSearchResults(query: string): void {
    this.searchResultService.getSearchResults(query, this.useSVD)
      .then(searchResults => this.results = searchResults)
      .catch(() => {}) // nice error handling tho
  }

  updateDocument(documentPath: string): void {
    this.documentService.getDocument(documentPath)
      .then(document => this.document = document)
      .catch(() => {})
  }
}
