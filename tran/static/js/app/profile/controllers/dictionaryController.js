/**
 * Контроллер словаря
 */
function DictionaryController ($scope, Dictionary, Profile, focusFactory) {
    this.focus = focusFactory;
    this.$scope = $scope;
    $scope.profile = Profile;
    $scope.dict = Dictionary;
    this.bindScope();

    $scope.$watch('dict.allExport', function(value) {
        if (value === true) {
            $scope.dict.checkAllExport();
        } else if (value === false) {
            $scope.dict.uncheckAllExport();
        }
    });
}

DictionaryController.prototype = {
    bindScope: function () {
        this.$scope.exportCheck = this.exportCheck.bind(this);
        this.$scope.doExport = this.doExport.bind(this);
        this.$scope.addWord = this.addWord.bind(this);
    },

    /** Добавление слова */
    addWord: function (e) {
        e.preventDefault();
        this.$scope.dict.nWord.language = this.$scope.currentLanguage;
        // после успешной отправки слова, сбрасываем форму для валидации
        this.$scope.dict.addWord().then(function () {
            this.$scope.wordform.$setPristine();
            this.focus.event('new.word');
        }.bind(this))
    },

    exportCheck: function (wordId) {
        console.log(wordId);
    },

    doExport: function () {
        var params = this.$scope.dict.getExportParams();
        var url = '/export/?' + params;
        location.href = url;
    }
}

DictionaryController.$inject = ['$scope', 'Dictionary', 'Profile', 'focusFactory'];

module.exports = DictionaryController;