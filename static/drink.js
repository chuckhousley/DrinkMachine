var DrinkApp = angular.module('DrinkApp', []);

function test($scope, $http) {
    $http.get('http://127.0.0.1:5000/api/drink').success(function(data){
        $scope.test1 = data;
        console.log($scope.test1.toString());
    });
}

