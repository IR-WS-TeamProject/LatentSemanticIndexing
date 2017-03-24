# Ui

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 1.0.0.

To run anything you need to `npm install -g @angular/cli`

## Plug into server (todo)

The search-result-service expects an api with a url. This front end expects to send a GET-request of following type: `/api?query=bli%20bla%20blub` and receivs an object of following type:
```json
{
data: [{
	title: 'bli',
	url: 'http://www.bli.com'
}, {
	title: 'bla',
	url: 'http://www.bla.com'
}, ...]
}
```

## Development server

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The app will automatically reload if you change any of the source files.

## Code scaffolding

Run `ng generate component component-name` to generate a new component. You can also use `ng generate directive/pipe/service/class/module`.

## Build

Run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory. Use the `-prod` flag for a production build.

## Further help

To get more help on the Angular CLI use `ng help` or go check out the [Angular CLI README](https://github.com/angular/angular-cli/blob/master/README.md).
