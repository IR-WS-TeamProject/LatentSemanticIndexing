webpackJsonp([1,4],{

/***/ 136:
/***/ (function(module, exports, __webpack_require__) {

exports = module.exports = __webpack_require__(45)();
// imports


// module
exports.push([module.i, ".content, input {\n\tmargin: 0 0 0 20px;\n}\n\ninput {\n\tfont-size: 1.2em;\n\tborder: none;\n}\n\nul {\n\tlist-style-type: none;\n\tpadding: 0;\n\tmargin: 15px 0 0 0;\n\twidth: 40%;\n\tfloat: left;\n}\n\nli {\n\tmargin: 0 0 8px 0;\n\tbackground-color: white;\n\tpadding: 7px 15px 10px 15px;\n}\n\nli:hover {\n\tbox-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n}\n\nli h2 {\n\tmargin: 0 0 4px 0;\n}\n\n.document {\n\twhite-space: pre-wrap;\n\tfloat: right;\n\twidth: 40%;\n\tmargin: 0 15% 0 0;\n}", ""]);

// exports


/*** EXPORTS FROM exports-loader ***/
module.exports = module.exports.toString();

/***/ }),

/***/ 138:
/***/ (function(module, exports) {

module.exports = "<div class=\"app\">\n\t<h1>\n\t\t{{title}}\n\t</h1>\n\t<input [(ngModel)]=\"query\" placeholder=\"Query\" (keyup.enter)=\"updateSearchResults(query)\">\n\t<button (click)=\"switchMode()\">{{buttonText}}</button><span>{{labelText}}</span>\n\t<div class=\"content\">\n\t\t<ul>\n\t\t\t<li *ngFor=\"let result of results\">\n\t\t\t\t<a (click)=\"updateDocument(result.doc)\">\n\t\t\t\t\t<h2>{{result.doc}}</h2>\n\t\t\t\t\t<p>{{result.rank}}</p>\n\t\t\t  \t</a>\n\t\t\t</li>\n\t\t</ul>\n\t\t<div class=\"document\">\n\t\t\t{{document}}\n\t\t</div>\n\t</div>\n</div>\n"

/***/ }),

/***/ 164:
/***/ (function(module, exports, __webpack_require__) {

module.exports = __webpack_require__(74);


/***/ }),

/***/ 49:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__(4);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__angular_http__ = __webpack_require__(28);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2_rxjs_add_operator_toPromise__ = __webpack_require__(64);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2_rxjs_add_operator_toPromise___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_2_rxjs_add_operator_toPromise__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return DocumentService; });
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};



var DocumentService = (function () {
    function DocumentService(http) {
        this.http = http;
        this.apiUrl = '/api?doc=';
    }
    DocumentService.prototype.getDocument = function (documentPath) {
        console.log("Get document " + documentPath);
        var url = "" + this.apiUrl + documentPath;
        return this.http.get(url)
            .toPromise()
            .then(function (response) { return response.text(); })
            .catch(this.handleError);
    };
    DocumentService.prototype.handleError = function (error) {
        return Promise.reject(error.message || error);
    };
    return DocumentService;
}());
DocumentService = __decorate([
    __webpack_require__.i(__WEBPACK_IMPORTED_MODULE_0__angular_core__["c" /* Injectable */])(),
    __metadata("design:paramtypes", [typeof (_a = typeof __WEBPACK_IMPORTED_MODULE_1__angular_http__["b" /* Http */] !== "undefined" && __WEBPACK_IMPORTED_MODULE_1__angular_http__["b" /* Http */]) === "function" && _a || Object])
], DocumentService);

var _a;
//# sourceMappingURL=document.service.js.map

/***/ }),

/***/ 50:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__(4);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__angular_http__ = __webpack_require__(28);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2_rxjs_add_operator_toPromise__ = __webpack_require__(64);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2_rxjs_add_operator_toPromise___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_2_rxjs_add_operator_toPromise__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return SearchResultsService; });
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};



var SearchResultsService = (function () {
    function SearchResultsService(http) {
        this.http = http;
        this.apiUrl = '/api?query=';
    }
    SearchResultsService.prototype.getSearchResults = function (query, withSVD) {
        if (withSVD === void 0) { withSVD = true; }
        console.log("Find documents for: " + query);
        // return Promise.resolve(SEARCH_RESULTS)
        var url = "" + this.apiUrl + encodeURI(query) + "&svd=" + withSVD;
        return this.http.get(url)
            .toPromise()
            .then(function (response) { return response.json(); })
            .catch(this.handleError);
    };
    SearchResultsService.prototype.handleError = function (error) {
        return Promise.reject(error.message || error);
    };
    return SearchResultsService;
}());
SearchResultsService = __decorate([
    __webpack_require__.i(__WEBPACK_IMPORTED_MODULE_0__angular_core__["c" /* Injectable */])(),
    __metadata("design:paramtypes", [typeof (_a = typeof __WEBPACK_IMPORTED_MODULE_1__angular_http__["b" /* Http */] !== "undefined" && __WEBPACK_IMPORTED_MODULE_1__angular_http__["b" /* Http */]) === "function" && _a || Object])
], SearchResultsService);

var _a;
//# sourceMappingURL=search-results.service.js.map

/***/ }),

/***/ 73:
/***/ (function(module, exports) {

function webpackEmptyContext(req) {
	throw new Error("Cannot find module '" + req + "'.");
}
webpackEmptyContext.keys = function() { return []; };
webpackEmptyContext.resolve = webpackEmptyContext;
module.exports = webpackEmptyContext;
webpackEmptyContext.id = 73;


/***/ }),

/***/ 74:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__(4);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__angular_platform_browser_dynamic__ = __webpack_require__(79);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__app_app_module__ = __webpack_require__(81);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__environments_environment__ = __webpack_require__(82);




if (__WEBPACK_IMPORTED_MODULE_3__environments_environment__["a" /* environment */].production) {
    __webpack_require__.i(__WEBPACK_IMPORTED_MODULE_0__angular_core__["a" /* enableProdMode */])();
}
__webpack_require__.i(__WEBPACK_IMPORTED_MODULE_1__angular_platform_browser_dynamic__["a" /* platformBrowserDynamic */])().bootstrapModule(__WEBPACK_IMPORTED_MODULE_2__app_app_module__["a" /* AppModule */]);
//# sourceMappingURL=main.js.map

/***/ }),

/***/ 80:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__(4);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__search_results_service__ = __webpack_require__(50);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__document_service__ = __webpack_require__(49);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return AppComponent; });
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};



var AppComponent = (function () {
    function AppComponent(searchResultService, documentService) {
        this.searchResultService = searchResultService;
        this.documentService = documentService;
        this.title = 'Latent Semantic Indexing Search';
        this.query = null;
        this.results = null;
        this.document = '';
        this.buttonText = 'Use VSM';
        this.labelText = 'SVD Mode';
        this.svdMode = true;
    }
    AppComponent.prototype.ngOnInit = function () {
        /* this.searchResultService.getSearchResults('initial query?')
            .then(searchResults => this.results = searchResults)
          .catch(() => {}) // nice error handling tho */
    };
    AppComponent.prototype.updateSearchResults = function (query) {
        var _this = this;
        this.searchResultService.getSearchResults(query, this.svdMode)
            .then(function (searchResults) { return _this.results = searchResults; })
            .catch(function () { }); // nice error handling tho
    };
    AppComponent.prototype.updateDocument = function (documentPath) {
        var _this = this;
        this.documentService.getDocument(documentPath)
            .then(function (document) { return _this.document = document; })
            .catch(function () { });
    };
    AppComponent.prototype.switchMode = function () {
        this.svdMode = !this.svdMode;
        if (this.svdMode) {
            this.buttonText = 'Use VSM';
            this.labelText = 'SVD Mode';
        }
        else {
            this.buttonText = 'Use SVD';
            this.labelText = 'VSM Mode';
        }
    };
    return AppComponent;
}());
AppComponent = __decorate([
    __webpack_require__.i(__WEBPACK_IMPORTED_MODULE_0__angular_core__["_3" /* Component */])({
        selector: 'app-root',
        template: __webpack_require__(138),
        styles: [__webpack_require__(136)]
    }),
    __metadata("design:paramtypes", [typeof (_a = typeof __WEBPACK_IMPORTED_MODULE_1__search_results_service__["a" /* SearchResultsService */] !== "undefined" && __WEBPACK_IMPORTED_MODULE_1__search_results_service__["a" /* SearchResultsService */]) === "function" && _a || Object, typeof (_b = typeof __WEBPACK_IMPORTED_MODULE_2__document_service__["a" /* DocumentService */] !== "undefined" && __WEBPACK_IMPORTED_MODULE_2__document_service__["a" /* DocumentService */]) === "function" && _b || Object])
], AppComponent);

var _a, _b;
//# sourceMappingURL=app.component.js.map

/***/ }),

/***/ 81:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_platform_browser__ = __webpack_require__(20);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__angular_core__ = __webpack_require__(4);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__angular_forms__ = __webpack_require__(78);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__angular_http__ = __webpack_require__(28);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_4__app_component__ = __webpack_require__(80);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_5__search_results_service__ = __webpack_require__(50);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_6__document_service__ = __webpack_require__(49);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return AppModule; });
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};







var AppModule = (function () {
    function AppModule() {
    }
    return AppModule;
}());
AppModule = __decorate([
    __webpack_require__.i(__WEBPACK_IMPORTED_MODULE_1__angular_core__["b" /* NgModule */])({
        declarations: [
            __WEBPACK_IMPORTED_MODULE_4__app_component__["a" /* AppComponent */]
        ],
        imports: [
            __WEBPACK_IMPORTED_MODULE_0__angular_platform_browser__["a" /* BrowserModule */],
            __WEBPACK_IMPORTED_MODULE_2__angular_forms__["a" /* FormsModule */],
            __WEBPACK_IMPORTED_MODULE_3__angular_http__["a" /* HttpModule */]
        ],
        providers: [
            __WEBPACK_IMPORTED_MODULE_5__search_results_service__["a" /* SearchResultsService */],
            __WEBPACK_IMPORTED_MODULE_6__document_service__["a" /* DocumentService */]
        ],
        bootstrap: [__WEBPACK_IMPORTED_MODULE_4__app_component__["a" /* AppComponent */]]
    })
], AppModule);

//# sourceMappingURL=app.module.js.map

/***/ }),

/***/ 82:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return environment; });
// The file contents for the current environment will overwrite these during build.
// The build system defaults to the dev environment which uses `environment.ts`, but if you do
// `ng build --env=prod` then `environment.prod.ts` will be used instead.
// The list of which env maps to which file can be found in `.angular-cli.json`.
// The file contents for the current environment will overwrite these during build.
var environment = {
    production: false
};
//# sourceMappingURL=environment.js.map

/***/ })

},[164]);
//# sourceMappingURL=main.bundle.js.map