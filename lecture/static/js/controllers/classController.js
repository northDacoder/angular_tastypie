function classController($scope, $http) {
      $http.get('api/v1/class/?format=json').success(function(data){
            console.log(data);
      }).error(function(data){
            console.log("You have an error in your code");
      });
};
