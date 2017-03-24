import { Component, OnInit } from '@angular/core'

import { SearchResult } from './search-result'
import { SearchResultsService } from './search-results.service'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  private title = 'Latent Semantic Indexing Search'
  private query: string = null
  private results: SearchResult[] = null

  constructor(private searchResultService: SearchResultsService) { }

  ngOnInit() {
  	this.searchResultService.getSearchResults('initial query?')
  		.then(searchResults => this.results = searchResults)
      .catch(() => {}) // nice error handling tho
  }
}
