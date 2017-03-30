import { BrowserModule } from '@angular/platform-browser'
import { NgModule } from '@angular/core'
import { FormsModule } from '@angular/forms'
import { HttpModule } from '@angular/http'

import { AppComponent } from './app.component'
import { SearchResultsService } from './search-results.service'
import { DocumentService } from './document.service'

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule
  ],
  providers: [ 
    SearchResultsService,
    DocumentService
  ],
  bootstrap: [ AppComponent ]
})
export class AppModule { }
