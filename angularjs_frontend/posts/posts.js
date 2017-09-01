
app.controller('posts_controller', [
    '$scope', 'StatementService', '$location', '$interval', '$q', '$rootScope',
    function($scope, StatementService, $location, $interval, $q, $rootScope) {

        $scope.statements = [{'name': '0', 'slug': 'fake'}];
        $rootScope.page = $location.path();
    }

]);

