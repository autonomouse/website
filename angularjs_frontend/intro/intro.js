
app.controller('intro_controller', [
    '$scope', 'StatementService', '$location', '$interval', '$q', '$rootScope',
    function($scope, StatementService, $location, $interval, $q, $rootScope) {

        $scope.reload = function () {
            var response = StatementService.query();
            //var response = StatementService.get({'section.name': 'About'});
            if (angular.isUndefined($scope.statements)){
                $scope.statements = response;
            } else{
                $q.all([response.$promise]).then(function(data) {
                    $scope.statements = data[0];
                });
            };
        };
        $scope.reload();
        //$interval($scope.reload, 1000);
        $rootScope.page = $location.path();
    }

]);

