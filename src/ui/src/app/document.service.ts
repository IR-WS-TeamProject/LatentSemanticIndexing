import { Injectable } from '@angular/core';
import { Http } from '@angular/http'

import 'rxjs/add/operator/toPromise'

@Injectable()
export class DocumentService {

	private apiUrl: string = '/api?doc='

  constructor(private http: Http) { }

  getDocument(documentPath: string): Promise<string> {
    console.log(`Get document ${documentPath}`)
  	const url = `${this.apiUrl}${documentPath}`
  	return this.http.get(url)
      .toPromise()
      .then(response => response.text())
    	.catch(this.handleError)
  }

  private handleError(error: any): Promise<any> {
    return Promise.reject(error.message || error)
  }
}
