function classController($scope, $http, $routeParams) {
      $http.get('api/v1/class/' + $routeParams.id + '?format=json').success(function(data){

          console.log(data);
          $scope.class = data;
          $scope.students = data.students;
          $scope.title = students.title;

//          var classobj = data.objects;
//          console.log(classobj);
//          for (var i = 0; i < classobj.length; i++) {
//              console.log(classobj[i]);
//              cohorts.push(classobj[i]);
//          }

      }).error(function(data){
          console.log("You have an error in your code");
      });
};
