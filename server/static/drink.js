(function () {
    var app = angular.module('DrinkApp', [], function($interpolateProvider) {
        $interpolateProvider.startSymbol('[[');
        $interpolateProvider.endSymbol(']]');
    });

    app.controller('DrinkController', function($http, $scope) {
        $http.get('/api/drink').success(function(data) {
            $scope.drinks = data.objects;
            console.info("[*] " + $scope.drinks.length)
        }).error(function(status) {
            console.error('error');
        });
    });
})();
