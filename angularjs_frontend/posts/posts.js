
app.controller('posts_controller', [
    '$scope', 'StatementService', '$interval', '$q',
    function($scope, StatementService, $interval, $q) {

        $scope.statements = [{'name': '0', 'slug': 'fake'}];
    }
]);

