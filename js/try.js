
var app = angular.module('myApp', ['ui.router']);
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
          $scope.date = new Date();        
          $scope.submit = function() {
        if ($scope.text) {
            $scope.list.push(this.text);
            $scope.getData = {'log_remark':'You searched for: ', 'comment':$scope.text};
            $scope.getSearch = {'log_remark':'You searched for: ', 'comment':$scope.text, 'Date':$scope.date};
            $http({
                  url: 'http://localhost:8080/logSearch',
                  method: "POST",
                  data: $scope.getSearch
              })
              .then(function(response) {
                  console.log("Searched data");
              });
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
            $scope.text = '';
            }
          }
      });



  app.controller('synoCtrl', function($scope, $http) {
//================================================//
  $scope.choices = [{}];
  $scope.addNewChoice = function() {
    var newItemNo = $scope.choices.length+1;
    $scope.choices.push({newItemNo});
  };
  //================================================//
  $scope.removeChoice = function() {
    var lastItem = $scope.choices.length-1;
    $scope.choices.splice(lastItem);
  };
//================================================//
  $scope.keywords = [{}];
  $scope.addNewkeyword = function() {
    var keynewItemNo = $scope.keywords.length+1;
    $scope.keywords.push({keynewItemNo});
  };
//================================================//
  $scope.removekeyword = function() {
    var keylastItem = $scope.keywords.length-1;
    $scope.keywords.splice(keylastItem);
  };
//================================================//
 $scope.submit = function() {
  $scope.compilation=[];
  $scope.compilation.push($scope.keywords,$scope.choices,$scope.text);
  $http({
        url: 'http://localhost:8080/addSearch',
        method: "POST",
        data: $scope.compilation
    })
    .then(function(response) {
        console.log("Searched data here");
        location.reload();
    });
 }
});
//================================================//




//================================================//
app.controller('dictionary_list', function($scope, $http) {
  $http({
        url: 'http://localhost:8080/things',
        method: "GET",
    })
    .then(function(response) {
        console.log("Searched data here");
        console.log(response.data);
        $scope.compilation = response.data;
        console.log($scope.compilation);
    });
//================================================//
     $scope.deleteDictForm = function() {
      console.log($scope.getData);
      location.reload();
    $http({
        url: 'http://localhost:8080/getDelete',
        method: "POST",
        data: $scope.getData
    })
    .then(function(response) {
        console.log("Searched data here");
      
      });

    }
//================================================//
     $scope.deleteDict = function(data){
      $scope.getData = data;
     }
//================================================//
     $scope.editDict = function(data){
      $scope.getId = data.id;
      $scope.keywords = data.value.keywords;      
      $scope.syno = data.value.synonymous;
      $scope.job_title = data.value.job_title;
      console.log($scope.syno);
     }
//================================================//
      $scope.deleteSyno = function(data) { 
        var index = $scope.syno.indexOf(data);
        $scope.removeSyno = {'syno':data,'id':$scope.getId};

        $scope.syno.splice(index, 1);
        $http({
              url: 'http://localhost:8080/delSyno',
              method: "POST",
              data: $scope.removeSyno
              })
          .then(function(response) {
              console.log("del Syno");
              });
            }
//================================================//
      $scope.deleteKeywords = function(data) { 
        console.log(data);
        var index = $scope.keywords.indexOf(data);
        $scope.removekeyword = {'keywords':data,'id':$scope.getId};

        $scope.keywords.splice(index, 1);  


        $http({
              url: 'http://localhost:8080/delKeywords',
              method: "POST",
              data: $scope.removekeyword
              })
          .then(function(response) {
              console.log("del Keyword");
              });
}
//================================================//
      $scope.UpdateSyno = function(data,placeholder) { 
        $scope.CurrentSyno = placeholder // orig value
        $scope.NewSyno = data //new value
        console.log(placeholder)
        $scope.updateSyno = {'CurrentSyno':placeholder,'NewSyno':data,'id':$scope.getId};
        console.log($scope.updateSyno);
        $http({
              url: 'http://localhost:8080/UpdateSyno',
              method: "POST",
              data: $scope.updateSyno
              })
          .then(function(response) {
              console.log("UpdateSyno");
              });
            }
//================================================//
      $scope.updateKeywords = function(data,placeholder) { 
        $scope.CurrentKeyword = placeholder // orig value
        $scope.NewKeyword = data //new value
        console.log(placeholder)
        $scope.updateKeyword = {'CurrentKeyword':placeholder,'NewKeyword':data,'id':$scope.getId};
        console.log($scope.updateKeyword);
        $http({
              url: 'http://localhost:8080/UpdateKeywords',
              method: "POST",
              data: $scope.updateKeyword
              })
          .then(function(response) {
              console.log("UpdateKeyword");
              });
            

          }
//================================================//

      $scope.UpdateJobTitle = function(data) { 
        $scope.UpdateJobTitle = {'job_title':data,'id':$scope.getId};
        $http({
              url: 'http://localhost:8080/UpdateJobTitle',
              method: "POST",
              data: $scope.UpdateJobTitle
          })
          .then(function(response) {
              console.log("UpdateJobTitle");
          });
        }
});
//================================================//




//================================================//
app.config(function($stateProvider) {
  var helloState = {
    name: 'hello',
    url: '/hello',
    templateUrl: './dict.html'
  }

  var aboutState = {
    name: 'about',
    url: '/about',
    template: '<h3>Its the UI-Router hello world app!</h3>'
  }

  $stateProvider.state(helloState);
  $stateProvider.state(aboutState);
});
//================================================//