import { Component, OnInit } from '@angular/core'

import { SearchResult } from './search-result'
import { SearchResultsService } from './search-results.service'
import { DocumentService } from './document.service'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  private title = 'Latent Semantic Indexing Search'
  private query: string = null
  private results: SearchResult[] = null
  private document: string = ''

  constructor(
    private searchResultService: SearchResultsService,
    private documentService: DocumentService
  ) { }

  ngOnInit() {
  	/* this.searchResultService.getSearchResults('initial query?')
  		.then(searchResults => this.results = searchResults)
      .catch(() => {}) // nice error handling tho */
  }

  updateSearchResults(query: string): void {
    this.searchResultService.getSearchResults(query)
      .then(searchResults => this.results = searchResults)
      .catch(() => {}) // nice error handling tho
  }

  updateDocument(documentPath: string): void {
    this.documentService.getDocument(documentPath)
      .then(document => this.document = document)
      .catch(() => {})
  }
}
