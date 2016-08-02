function DictionaryModel (ActiveRecord) {
    return ActiveRecord.extend({

        $constructor: function DictionaryModel () {
            this.$initialize.apply(this, arguments);
        },
    });
}

DictionaryModel.$inject = ['ActiveRecord'];

module.exports = DictionaryModel;