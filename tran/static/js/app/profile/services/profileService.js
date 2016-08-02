var ProfileService = function () {
    this.language = 'english';
}

ProfileService.prototype = {
    setLanguage: function (language) {
        this.language = language;
    },

    getLanguage: function () {
        return this.language;
    }
}

module.exports = ProfileService;