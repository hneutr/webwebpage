function changeCodeDisplay(selectlist) {
    var languages = [];
    for (var i in selectlist.options) {
        var language = selectlist.options[i].value;

        if (language !== undefined) {
            language = language.replace(/\s/g, '');
            languages.push(language);
        }
    }

    var languageIndex = selectlist.selectedIndex;
    var selectedLanguage = languages[languageIndex];

    for (var i in languages) {
        var language = languages[i];
        var languageCodeElement = document.getElementById(language + '-code-block');

        if (language == selectedLanguage) {
            languageCodeElement.classList.add("select-code-block-visible");

        }
        else {
            languageCodeElement.classList.remove("select-code-block-visible");
        }
    }
}
