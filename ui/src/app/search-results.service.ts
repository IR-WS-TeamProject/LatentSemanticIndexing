import { Injectable } from '@angular/core'
import { Http } from '@angular/http'

import 'rxjs/add/operator/toPromise'

import { SearchResult } from './search-result'
import { SEARCH_RESULTS } from './search-results.mock'

@Injectable()
export class SearchResultsService {

	private apiUrl: string = '/api?query='

  constructor(private http: Http) { }

  getSearchResults(query: string): Promise<SearchResult[]> {
  	// return Promise.resolve(SEARCH_RESULTS)
  	const url = `${this.apiUrl}${encodeURI(query)}`
  	return this.http.get(url)
     .toPromise()
     .then(response => response.json().data as SearchResult[])
     .catch(this.handleError)
  }

  private handleError(error: any): Promise<any> {
    return Promise.reject(error.message || error)
  }
}
