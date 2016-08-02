'use strict';
var profileController = require('./controllers/profileController.js');
var dictionaryController = require('./controllers/dictionaryController.js');
var currentLanguageDirective = require('./directives/currentLanguageDirective.js');
var DictionaryModel = require('./models/dictionaryModel.js');
var DictionaryService = require('./services/dictionaryService.js');
var FocusFactory = require('./services/focusFactory.js');

var ProfileService = require('./services/profileService.js');
var FocusOn = require('./directives/focusOn.js');

var profileModule = angular.module('tran.profile', [])
    .service('Profile', ProfileService)
    .service('Dictionary', DictionaryService)
    .factory('DictionaryModel', DictionaryModel)
    .service('focusFactory', FocusFactory)

    .controller('ProfileController', profileController)
    .controller('DictionaryController', dictionaryController)
    .directive('currentLang', currentLanguageDirective)
    .directive('focusOn', FocusOn);
