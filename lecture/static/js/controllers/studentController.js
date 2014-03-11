function studentController($scope, $http) {
    $http.get('api/v1/student/?format=json').success(function(data){
        console.log(data);

    }).error(function(data){
        console.log("You have an error in your code");
    });


    $scope.user = {'klass': "api/v1/class/1/", 'projects':[]};

    $scope.addStudent = function() {
        console.log($scope.user);
        $http:post('api/v1/student/', $scope.user).success(function(){
            alert('Add a student?');
        });
    }

    $scope.deleteStudent = function() {
        console.log($scope.user);
        $http:delete('api/v1/student/', $scope.user).success(function(){
            alert('You are trying to delete a student!');
        });
    }
};
