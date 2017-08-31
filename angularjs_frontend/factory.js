
app.factory('StatementService', ['$resource', function($resource) {
    return $resource('http://127.0.0.1:8000/api/statement/:statement',
                     {statement: "@statement"});
}]);
