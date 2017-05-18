webpackJsonp([1,4],{

/***/ 140:
/***/ (function(module, exports, __webpack_require__) {

exports = module.exports = __webpack_require__(45)();
// imports


// module
exports.push([module.i, ".content, input {\n\tmargin: 0 0 0 20px;\n}\n\n.svdSwitch {\n\tmargin: 0 0 13px 17px;\n\tvertical-align: middle;\n}\n\ninput {\n\tfont-family: serif;\n\tfont-size: 1.2em;\n\tborder: none;\n}\n\ntable {\n\tmargin: 10px 0 10px 20px;\n}\n\ntable, th, td {\n    border: 1px solid black;\n}\n\nul {\n\toverflow-y: scroll;\n\theight: 550px;\n\tlist-style-type: none;\n\tpadding: 0;\n\tmargin: 15px 0 0 0;\n\twidth: 40%;\n\tfloat: left;\n}\n\nli div {\n\tmargin: 0 0 8px 0;\n\tbackground-color: white;\n\tpadding: 7px 15px 10px 15px;\n}\n\n.bordered {\n\tborder: black;\n\tborder-style: solid;\n\tborder-width: thick;\n}\n\nli:hover {\n\tbox-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n}\n\nli h2 {\n\tmargin: 0 0 4px 0;\n}\n\n.document {\n\toverflow-y: scroll;\n\theight: 550px;\n\twhite-space: pre-wrap;\n\tfloat: right;\n\twidth: 40%;\n\tmargin: 0 15% 0 0;\n}\n", ""]);

// exports


/*** EXPORTS FROM exports-loader ***/
module.exports = module.exports.toString();

/***/ }),

/***/ 144:
/***/ (function(module, exports) {

module.exports = "<div class=\"app\">\n\t<ui-switch [(ngModel)]=\"evaluationMode\" style=\"visibility:visible; position:absolute; right:50px;\"></ui-switch>\n\t<h1>\n\t\t{{title}}<span *ngIf=\"evaluationMode\"> (evaluation mode)</span>\n\t</h1>\n\t<div *ngIf=\"!evaluationMode\" class=\"svdSwitch\">Use SVD:&nbsp;<ui-switch [(ngModel)]=\"useSVD\" size=\"small\"></ui-switch></div>\n\t<input [(ngModel)]=\"query\" placeholder=\"Query\" (keyup.enter)=\"updateSearchResults(query)\">\n\t<button (click)=\"updateSearchResults(query)\">Search</button><span *ngIf=\"results\">{{results.length}} results</span>\n\t<table *ngIf=\"evaluationMode\">\n\t\t<thead>\n\t\t\t<th>SVD Avg</th>\n\t\t\t<th>SVD R</th>\n\t\t\t<th>VSM Avg</th>\n\t\t\t<th>VSM R</th>\n\t\t</thead>\n\t\t<tbody>\n\t\t\t<tr>\n\t\t\t\t<td>{{svdAvgPrecision}}</td>\n\t\t\t\t<td>{{svdRPrecision}}</td>\n\t\t\t\t<td>{{vsmAvgPrecision}}</td>\n\t\t\t\t<td>{{vsmRPrecision}}</td>\n\t\t\t</tr>\n\t\t</tbody>\n\t</table>\n\t<div class=\"content\">\n\t\t<ul>\n\t\t\t<li *ngFor=\"let result of results\">\n\t\t\t\t<div [ngClass]=\"{'bordered': result.doc === selected}\">\n\t\t\t\t\t<a (click)=\"updateDocument(result.doc)\">\n\t\t\t\t\t\t<h2>{{result.doc}}</h2>\n\t\t\t\t\t\t<p>{{result.rank}}</p>\n\t\t\t\t\t</a>\n\t\t\t\t\t<ui-switch *ngIf=\"evaluationMode\" (change)=\"calculatePrecision($event, result, query)\"></ui-switch>\n\t\t\t\t</div>\n\t\t\t</li>\n\t\t</ul>\n\t\t<div class=\"document\">\n\t\t\t{{document}}\n\t\t</div>\n\t</div>\n</div>\n"

/***/ }),

/***/ 171:
/***/ (function(module, exports, __webpack_require__) {

module.exports = __webpack_require__(77);


/***/ }),

/***/ 51:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__(3);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__angular_http__ = __webpack_require__(28);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2_rxjs_add_operator_toPromise__ = __webpack_require__(67);
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

/***/ 52:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__(3);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__angular_http__ = __webpack_require__(28);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2_rxjs_add_operator_toPromise__ = __webpack_require__(67);
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
    SearchResultsService.prototype.getSearchResults = function (query, withSVD, count) {
        if (withSVD === void 0) { withSVD = true; }
        console.log("Find documents for: " + query);
        // return Promise.resolve(SEARCH_RESULTS)
        var countString = count ? "&count=" + count : '';
        var url = "" + this.apiUrl + encodeURI(query) + "&svd=" + withSVD + countString;
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

/***/ 76:
/***/ (function(module, exports) {

function webpackEmptyContext(req) {
	throw new Error("Cannot find module '" + req + "'.");
}
webpackEmptyContext.keys = function() { return []; };
webpackEmptyContext.resolve = webpackEmptyContext;
module.exports = webpackEmptyContext;
webpackEmptyContext.id = 76;


/***/ }),

/***/ 77:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__(3);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__angular_platform_browser_dynamic__ = __webpack_require__(81);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__app_app_module__ = __webpack_require__(83);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__environments_environment__ = __webpack_require__(85);




if (__WEBPACK_IMPORTED_MODULE_3__environments_environment__["a" /* environment */].production) {
    __webpack_require__.i(__WEBPACK_IMPORTED_MODULE_0__angular_core__["a" /* enableProdMode */])();
}
__webpack_require__.i(__WEBPACK_IMPORTED_MODULE_1__angular_platform_browser_dynamic__["a" /* platformBrowserDynamic */])().bootstrapModule(__WEBPACK_IMPORTED_MODULE_2__app_app_module__["a" /* AppModule */]);
//# sourceMappingURL=main.js.map

/***/ }),

/***/ 82:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__(3);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_bluebird__ = __webpack_require__(86);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_bluebird___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_1_bluebird__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2_lodash__ = __webpack_require__(141);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2_lodash___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_2_lodash__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__search_result__ = __webpack_require__(84);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_4__search_results_service__ = __webpack_require__(52);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_5__document_service__ = __webpack_require__(51);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return AppComponent; });
var __extends = (this && this.__extends) || (function () {
    var extendStatics = Object.setPrototypeOf ||
        ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
        function (d, b) { for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p]; };
    return function (d, b) {
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};






var ExtendedSearchResult = (function (_super) {
    __extends(ExtendedSearchResult, _super);
    function ExtendedSearchResult() {
        var _this = _super !== null && _super.apply(this, arguments) || this;
        _this.relevant = false;
        return _this;
    }
    return ExtendedSearchResult;
}(__WEBPACK_IMPORTED_MODULE_3__search_result__["a" /* SearchResult */]));
var AppComponent = (function () {
    function AppComponent(searchResultService, documentService) {
        this.searchResultService = searchResultService;
        this.documentService = documentService;
        this.title = 'Latent Semantic Indexing Search';
        this.query = null;
        this.results = null;
        this.allSVDResults = null;
        this.allVSMResults = null;
        this.selected = null;
        this.document = '';
        this.useSVD = true;
        this.evaluationMode = false;
        this.svdResults = null;
        this.vsmResults = null;
        this.svdRPrecision = 0;
        this.vsmRPrecision = 0;
        this.svdAvgPrecision = 0;
        this.vsmAvgPrecision = 0;
    }
    AppComponent.prototype.updateSearchResults = function (query) {
        var _this = this;
        if (!this.evaluationMode) {
            this.searchResultService.getSearchResults(query, this.useSVD)
                .then(function (searchResults) { return _this.results = searchResults; })
                .catch(function () { }); // nice error handling tho
        }
        else {
            this.svdRPrecision = 0;
            this.vsmRPrecision = 0;
            this.svdAvgPrecision = 0;
            this.vsmAvgPrecision = 0;
            __WEBPACK_IMPORTED_MODULE_1_bluebird__["props"]({
                svdResults: this.searchResultService.getSearchResults(query, true, 11000),
                vsmResults: this.searchResultService.getSearchResults(query, false, 11000)
            }).then(function (data) {
                _this.allSVDResults = __WEBPACK_IMPORTED_MODULE_2_lodash__["map"](data.svdResults, function (_a) {
                    var doc = _a.doc;
                    return doc;
                });
                _this.allVSMResults = __WEBPACK_IMPORTED_MODULE_2_lodash__["map"](data.vsmResults, function (_a) {
                    var doc = _a.doc;
                    return doc;
                });
                _this.results = __WEBPACK_IMPORTED_MODULE_2_lodash__["shuffle"](__WEBPACK_IMPORTED_MODULE_2_lodash__["unionBy"](__WEBPACK_IMPORTED_MODULE_2_lodash__["slice"](data.svdResults, 0, 10), __WEBPACK_IMPORTED_MODULE_2_lodash__["slice"](data.vsmResults, 0, 10), 'doc'));
                _this.svdResults = data.svdResults;
                _this.vsmResults = data.vsmResults;
            });
        }
    };
    AppComponent.prototype.updateDocument = function (documentPath) {
        var _this = this;
        this.selected = documentPath;
        this.documentService.getDocument(documentPath)
            .then(function (document) { return _this.document = document; })
            .catch(function () { });
    };
    AppComponent.prototype.calculatePrecision = function (event, result, query) {
        result.relevant = event;
        var relevantDocuments = __WEBPACK_IMPORTED_MODULE_2_lodash__["chain"](this.results)
            .groupBy('relevant')
            .filter(function (val, key) { return key === 'true'; })
            .flatten()
            .map(function (_a) {
            var doc = _a.doc;
            return doc;
        })
            .value();
        var rankedDocumentsSVD = this.allSVDResults;
        var rankedDocumentsVSM = this.allVSMResults;
        var svdAvgPrecision = this.calculateAvgPrecision(rankedDocumentsSVD, relevantDocuments) || 0;
        var vsmAvgPrecision = this.calculateAvgPrecision(rankedDocumentsVSM, relevantDocuments) || 0;
        var svdRPrecision = this.calculateRPrecision(rankedDocumentsSVD, relevantDocuments) || 0;
        var vsmRPrecision = this.calculateRPrecision(rankedDocumentsVSM, relevantDocuments) || 0;
        this.svdAvgPrecision = parseFloat(svdAvgPrecision.toFixed(3));
        this.vsmAvgPrecision = parseFloat(vsmAvgPrecision.toFixed(3));
        this.svdRPrecision = parseFloat(svdRPrecision.toFixed(3));
        this.vsmRPrecision = parseFloat(vsmRPrecision.toFixed(3));
    };
    AppComponent.prototype.calculateAvgPrecision = function (rankedDocuments, relevantDocuments) {
        var sumOfPrecisions = __WEBPACK_IMPORTED_MODULE_2_lodash__["chain"](rankedDocuments)
            .map(function (doc, rank) { return ({ doc: doc, rank: rank + 1 }); })
            .filter(function (_a) {
            var doc = _a.doc;
            return __WEBPACK_IMPORTED_MODULE_2_lodash__["includes"](relevantDocuments, doc);
        })
            .map(function (_a, index) {
            var rank = _a.rank;
            return ((index + 1) / rank);
        })
            .tap(function (array) {
            if (array.length !== relevantDocuments.length) {
                console.log("Only found " + array.length + " relevant documents. Expected " + relevantDocuments.length + ".");
            }
        })
            .sum()
            .value();
        var precision = sumOfPrecisions / relevantDocuments.length;
        return precision;
    };
    AppComponent.prototype.calculateRPrecision = function (rankedDocuments, relevantDocuments) {
        if (relevantDocuments.length > rankedDocuments.length)
            return null;
        var slicedRankedDocuments = __WEBPACK_IMPORTED_MODULE_2_lodash__["slice"](rankedDocuments, 0, relevantDocuments.length);
        var countTruePositives = __WEBPACK_IMPORTED_MODULE_2_lodash__["sumBy"](slicedRankedDocuments, function (doc) { return __WEBPACK_IMPORTED_MODULE_2_lodash__["includes"](relevantDocuments, doc); });
        var precision = countTruePositives / relevantDocuments.length;
        return precision;
    };
    return AppComponent;
}());
AppComponent = __decorate([
    __webpack_require__.i(__WEBPACK_IMPORTED_MODULE_0__angular_core__["_1" /* Component */])({
        selector: 'app-root',
        template: __webpack_require__(144),
        styles: [__webpack_require__(140)]
    }),
    __metadata("design:paramtypes", [typeof (_a = typeof __WEBPACK_IMPORTED_MODULE_4__search_results_service__["a" /* SearchResultsService */] !== "undefined" && __WEBPACK_IMPORTED_MODULE_4__search_results_service__["a" /* SearchResultsService */]) === "function" && _a || Object, typeof (_b = typeof __WEBPACK_IMPORTED_MODULE_5__document_service__["a" /* DocumentService */] !== "undefined" && __WEBPACK_IMPORTED_MODULE_5__document_service__["a" /* DocumentService */]) === "function" && _b || Object])
], AppComponent);

var _a, _b;
//# sourceMappingURL=app.component.js.map

/***/ }),

/***/ 83:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_platform_browser__ = __webpack_require__(21);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__angular_core__ = __webpack_require__(3);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__angular_forms__ = __webpack_require__(50);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__angular_http__ = __webpack_require__(28);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_4_ng2_ui_switch__ = __webpack_require__(142);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_5__app_component__ = __webpack_require__(82);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_6__search_results_service__ = __webpack_require__(52);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_7__document_service__ = __webpack_require__(51);
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
            __WEBPACK_IMPORTED_MODULE_5__app_component__["a" /* AppComponent */]
        ],
        imports: [
            __WEBPACK_IMPORTED_MODULE_0__angular_platform_browser__["a" /* BrowserModule */],
            __WEBPACK_IMPORTED_MODULE_2__angular_forms__["a" /* FormsModule */],
            __WEBPACK_IMPORTED_MODULE_3__angular_http__["a" /* HttpModule */],
            __WEBPACK_IMPORTED_MODULE_4_ng2_ui_switch__["a" /* UiSwitchModule */]
        ],
        providers: [
            __WEBPACK_IMPORTED_MODULE_6__search_results_service__["a" /* SearchResultsService */],
            __WEBPACK_IMPORTED_MODULE_7__document_service__["a" /* DocumentService */]
        ],
        bootstrap: [__WEBPACK_IMPORTED_MODULE_5__app_component__["a" /* AppComponent */]]
    })
], AppModule);

//# sourceMappingURL=app.module.js.map

/***/ }),

/***/ 84:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return SearchResult; });
var SearchResult = (function () {
    function SearchResult() {
    }
    return SearchResult;
}());

//# sourceMappingURL=search-result.js.map

/***/ }),

/***/ 85:
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

},[171]);
//# sourceMappingURL=main.bundle.js.map