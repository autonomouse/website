var app = angular.module('App', [
    'ngRoute',
    'ngResource']);

    app.config(['$routeProvider', function($routeProvider) {
        $routeProvider.when('/:page', {
            templateUrl: 'section/section.html',
            controller: 'section_controller'
        })
}]);
