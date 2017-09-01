
app.controller('section_controller', [
    '$scope', 'SectionService', 'StatementService', '$location', '$interval', '$q', '$routeParams',
    function($scope, SectionService, StatementService, $location, $interval, $q, $routeParams) {

        $scope.page = $routeParams.page
        var sections = SectionService.query({"page__slug": $routeParams.page});
        var statements = {};
        $q.all([sections.$promise]).then(function([data]) {
            $scope.sections = data;
            angular.forEach(data, function(datum) {
                statements[datum.name] = StatementService.query({section__uuid: datum.uuid});
            });
            $scope.statements = statements;
        });
    }

]);

