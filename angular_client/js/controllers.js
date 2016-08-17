var app = angular.module("FibonacciApp");

app.controller("FibonacciController", function($scope, $http, $route){
    // $scope.header = 'Fibonacci Series';
});

app.controller("MainController", ['$scope', '$http', function($scope, $http){
    $scope.navbar = 'MathForFun.com';
    $scope.title = 'Fibonacci Series';
    $scope.condition = false;

    $scope.clearText = function(){
        // console.log("clearText called")
        $scope.number = null;
    };

    $scope.GetFibonacci = function(){
        console.log("GetFibonacci called");
        var num = $scope.number
        if ( !isNaN(num) && angular.isNumber(+num)) {
            // console.log(num)
            $scope.$parent.condition = true;
            url = 'http://localhost:9000/api/fibonacci/'
            $http({
                url: url, 
                method: "GET",
                params: {number: num}
             }).then(function(result){
                // console.log(result)
                $scope.$parent.exec_time = result['data']['data']['time'];
                $scope.$parent.fibo_value = result['data']['data']['value']
                $scope.$parent.fibo = result['data']['data']['fibo']
                $scope.number = null;
                // console.log('Execution time = ', $scope.exec_time + ' Value = ', $scope.fibo_value)

             })
    }
    else{
            alert('Please enter a number');
            $scope.number = null;
        }
}
}]);