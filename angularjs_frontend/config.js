var app = angular.module('App', [
    'ngRoute',
    'ngResource']);

    //app.config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider) {
    app.config(['$routeProvider', function($routeProvider) {
            $routeProvider
        .when('/about', {
            templateUrl: 'intro/intro.html',
            controller: 'intro_controller'
        })
        .when('/posts', {
            templateUrl: 'posts/posts.html',
            controller: 'posts_controller'
        })
        .otherwise({
            redirectTo: '/about'
        });
    // $locationProvider.html5Mode(true); // use the HTML5 History API
}]);
