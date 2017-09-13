
app.controller('main_controller', [
    '$scope', 'PageService', '$location', '$q', '$routeParams',
    function($scope, PageService, $location, $q, $routeParams) {

        $scope.SiteName = "Darren Hoyland";

        var response = PageService.query();
        $q.all([response.$promise]).then(function([data]) {
            $scope.pages = data;
        });

        $scope.isActive = function (viewLocation) {
              return viewLocation === $location.path();
        };

    }
]);

