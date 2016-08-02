/**
 * Сервис обработки добавления и редактирования слов
 * @param $http
 * @constructor
 */
var DictionaryService = function ($http) {
    this.$http = $http;
    this.words = [];
    this.total = 0;
    this.exportWords = [];
    this.fetchWords();
    this.allExport = false;
    this.$nameExist = true;
    this.$nameUnique = true;
    this.$pristine = true;
    this.nWord = {};
}
// Dict
DictionaryService.prototype = {
    addWord: function () {
        var self = this;
        return this.$http({
            method: 'POST',
            url: '/api/v2/words/',
            data: this.nWord
        }).success(function (response) {
            self.nWord = {};
            //TODO выполнять без доп. запроса
            return self.fetchWords();

        }).error(function (error) {
            console.log('error:', error);
        })
    },

    checkUnique: function () {
        if (this.wordExist(this.nWord.name)) {
            this.$nameUnique = false;
        } else {
            this.$nameUnique = true;
        }
        return this.$nameUnique;
    },

    wordExist: function (word) {
        word = word.toLowerCase();
        var len = this.words.length;
        var exist = false;
        while (len--) {
            if (this.words[len].name.toLowerCase() == word) {
                exist = true;
                break;
            }
        }
        return exist;
    },

    checkAllExport: function () {
        var len = this.words.length;
        while (len--) {
            this.words[len].export = true;
        }
    },

    uncheckAllExport: function () {
        var len = this.words.length;
        while (len--) {
            this.words[len].export = false;
        }
    },

    getExportParams: function () {
        var params = '';
        var len = this.words.length;
        while (len--) {
            if (this.words[len].export) {
                params += 'w=' + this.words[len].id  + '&';
            }
        }
        params = params.substring(0, params.length - 1);
        return params;
    },

    /* запрашивает все слова пользователя */
    fetchWords: function () {
        var self = this;
        return this.$http({
            method: 'GET',
            url: '/api/v2/words/'
            //data: {language: 'english'}
        }).then(
            function (res) {
                self.words = res.data.wordsList;
                self.total = res.data.total;
                return res.data.wordsList;
            }, 
            function (error) {
                return error;
            }
        )
    },

    /* удаляет слово из словаря */
    removeWord: function (id) {
        var self = this;
        this.deleteWordById(id);
        return this.$http({
            method: 'POST',
            url: '/api/v1/removeword/',
            data: {id: id}
        }).then(
            function (res) {
                self.total = self.words.length;
            },
            function (error) {
                console.log(error);
                return error;
            } 
        )
    },

    deleteWordById: function (id) {
        var len = this.words.length;
        while (len --) {
            if (this.words[len].id == id) {
                this.words.splice(len, 1);
            }
        }
    }
}

DictionaryService.$inject = ['$http'];

module.exports = DictionaryService;