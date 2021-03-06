import { Injectable } from '@angular/core'
import { Http } from '@angular/http'

import 'rxjs/add/operator/toPromise'

import { SearchResult } from './search-result'
import { SEARCH_RESULTS } from './search-results.mock'

@Injectable()
export class SearchResultsService {

	private apiUrl: string = '/api?query='

  constructor(private http: Http) { }

  getSearchResults(query: string, withSVD: boolean = true, count?: number): Promise<SearchResult[]> {
    console.log(`Find documents for: ${query}`)
  	// return Promise.resolve(SEARCH_RESULTS)
    const countString = count ? `&count=${count}` : ''
	  const url = `${this.apiUrl}${encodeURI(query)}&svd=${withSVD}${countString}`
  	return this.http.get(url)
     .toPromise()
     .then(response => response.json() as SearchResult[])
     .catch(this.handleError)
  }

  private handleError(error: any): Promise<any> {
    return Promise.reject(error.message || error)
  }
}
