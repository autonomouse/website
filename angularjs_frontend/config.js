var app = angular.module('App', [
    'ngRoute',
    'ngResource']);

app.config(['$routeProvider', function($routeProvider) {
    $routeProvider
        .when('/intro', {
            templateUrl: 'intro/intro.html',
            controller: 'controller',
            controllerAs:'controller'
        })
        .otherwise({
            redirectTo: '/intro'
        });
}]);
