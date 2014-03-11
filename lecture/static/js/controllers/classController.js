function classController($scope, $http) {
      $http.get('api/v1/class/?format=json').success(function(data){
          var cohorts = [];

          console.log(data);
          var classobj = data.objects;
          console.log(classobj);
          for (var i = 0; i < classobj.length; i++) {
              console.log(classobj[i]);
              cohorts.push(classobj[i]);
          }

          console.log(cohorts);
          $scope.cohorts = cohorts;
      }).error(function(data){
          console.log("You have an error in your code");
      });
};
