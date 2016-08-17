var app = angular.module("FibonacciApp", ['ngRoute']);

app.config(function($routeProvider){
    $routeProvider
        .when('/',{
            controller: 'MainController'
        })
        .otherwise({
            redirectTo: '/'
        });
});
