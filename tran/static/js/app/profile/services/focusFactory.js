var Focus = function ($rootScope, $timeout) {
  this.event = function (name) {
    $timeout(function (){
      $rootScope.$broadcast('focusOn', name);
    });
  }
};

Focus.$inject = ['$rootScope', '$timeout'];

module.exports = Focus;