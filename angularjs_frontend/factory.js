var url = 'http://127.0.0.1:8999/api/';

app.factory('PageService', ['$resource', function($resource) {
    return $resource(url + 'page/:page', {page: "@page"});
}]);

app.factory('SectionService', ['$resource', function($resource) {
    return $resource(url + 'section/:section', {section: "@section"});
}]);

app.factory('StatementService', ['$resource', function($resource) {
    return $resource(url + 'statement/:statement', {statement: "@statement"});
}]);
