
app.controller('intro_controller', [
    '$scope', 'StatementService', '$location', '$interval', '$q', '$rootScope',
    function($scope, StatementService, $location, $interval, $q, $rootScope) {

        $rootScope.page = $location.path();

        $scope.statements = StatementService.query();
        //var response = StatementService.get({'section.name': 'About'});

    }

]);

