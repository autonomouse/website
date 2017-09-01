
app.controller('section_controller', [
    '$scope', 'SectionService', '$location', '$interval', '$q', '$routeParams',
    function($scope, SectionService, $location, $interval, $q, $routeParams) {

        $scope.page = $routeParams.page
        $scope.sections = SectionService.query({"page__slug": $routeParams.page});
    }

]);

