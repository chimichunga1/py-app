
var app = angular.module('myApp', []);



      app.controller('HeaderCtrl', function($scope, $http) {
          $scope.greeting = "Hello World!";
          $http.get("http://localhost:8080/things").then(function(data){
            $scope.details = data.data;
            console.log($scope.details[0].value.job_title);
            $http.get("http://localhost:8080/things").then(function(data){
              $scope.dictionary=data.data
              log=[];
              counter_title=0;
              angular.forEach($scope.dictionary, function() {
                this.push($scope.dictionary[counter_title].value.job_title);
                counter_synonyms=0;
                counter_title++;
              },log);
              console.log(log);
              $( "#tags" ).autocomplete({
                source: log
              });
            });
          });
      });

      app.controller('ExampleController', function($scope, $http) {


          $scope.list = [];
          $scope.text = 'hello';        
          $scope.submit = function() {

        if ($scope.text) {
            $scope.list.push(this.text);           
            $scope.getData = {'log_remark':'JOB SEARCH', 'comment':$scope.text};
            $http({
                  url: 'http://localhost:8080/catchData',
                  method: "POST",
                  data: $scope.getData
              })
              .then(function(response) {
                  console.log("Checking");
                  console.log(response.data);
                  $scope.searchResult = response.data;
              });
            // $http.post('http://localhost:8080/catchData',$scope.getData).then(function(data){
            //   console.log("Checking");
            //   console.log(data);
            //   $scope.searchResult = data;
            // });
            //console.log($scope);
            $scope.text = '';
                          










                          }






          }
      });

