function indexController($scope, $http, RocketSpace) {

    console.log(RocketSpace.angular_instructor);
    console.log("indexController");

    $scope.classes = [];

    $http.get('api/v1/student/?format=json').success(function(data){
        console.log(data.objects);
        $scope.students = data.objects;
        RocketSpace.student_list = $scope.students;

    })
}