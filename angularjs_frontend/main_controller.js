
app.controller('main_controller', [
    '$scope', 'PageService', '$location', '$q',
    function($scope, PageService, $location, $q) {

        $scope.SiteName = "Darren Hoyland";

        var response = PageService.query();
        if (angular.isUndefined($scope.pages)){
            $scope.pages = response;
        } else{
            $q.all([response.$promise]).then(function(data) {
                $scope.pages = data[0];
            });
        };

        $scope.isActive = function (viewLocation) {
              return viewLocation === $location.path();
          };
    }
]);

