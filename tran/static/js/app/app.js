require('../vendors/angular/angular.js');
require('../vendors/angular-exts/angular-activerecord.js');
require('../vendors/angular/angular-animate.js');
require('../vendors/angular/angular-aria.js');
require('../vendors/angular/angular-material.js');

require('./profile/module.js');

var app = angular.module('tran', [
    'ngMaterial',
    'ActiveRecord',

    'tran.profile'
])

app.config(function($mdThemingProvider) {
  $mdThemingProvider.theme('default')
    .primaryPalette('blue')
    .accentPalette('brown');
});

app.filter("asDate", function () {
    return function (input) {
        return Date.parse(input);
    }
});