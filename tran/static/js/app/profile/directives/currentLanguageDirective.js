function CurrentLanguage (Profile) {
    return  {
        restrict: 'EA',
        link: function (scope, element, attrs) {
            var selector = element.find('select#language');
            var current = attrs.currentlang;
            selector.val(current);
            scope.currentLanguage = current;
            Profile.setLanguage(selector.find('option:selected').text());
            selector.on('change', function () {
                current = selector.val();
                window.location.search = 'lang='+current;
            });
        }
    }
}


CurrentLanguage.$inject = ['Profile' ];

module.exports = CurrentLanguage;