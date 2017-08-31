var app = angular.module('App', [
    'ngRoute',
    'ngResource']);

app.config(['$routeProvider', function($routeProvider) {
    $routeProvider
        .when('/', {
            //templateUrl: 'static/admin/admin.html',
            templateUrl: 'admin.html',
            controller: 'controller',
            controllerAs:'controller'
        })
}]);
