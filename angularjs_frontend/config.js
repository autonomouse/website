var app = angular.module('App', [
    'ngRoute',
    'ngResource']);

    app.config(['$routeProvider', '$httpProvider', function(
                $routeProvider, $httpProvider) {
        $routeProvider
            .when('/:page', {
                templateUrl: 'section/section.html',
                controller: 'section_controller'
            })
            .otherwise({
                redirectTo: '/about'
            });
        //$httpProvider.defaults.headers.common['X-CSRFToken'] = '{{ csrf_token|escapejs }}';
}]);
