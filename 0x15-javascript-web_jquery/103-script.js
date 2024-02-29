// fetches and prints how to say “Hello” depending on the language

// Wait for the document to be ready
$(document).ready(function () {
    // Function to fetch and display the translation
    function fetchTranslation() {
        // Get the language code from the input field
        let languageCode = $('#language_code').val();

        // Make an AJAX request to fetch the translation
        $.get(`https://www.fourtonfish.com/hellosalut/hello/${languageCode}`, function (data) {
            // Display the translation in the DIV#hello
            $('#hello').text(data.hello);
        });
    }

    // Trigger translation on button click
    $('#btn_translate').click(fetchTranslation);

    // Trigger translation on ENTER key press in the input field
    $('#language_code').keypress(function (event) {
        if (event.keyCode === 13) {
            // If ENTER key is pressed, fetch the translation
            fetchTranslation();
        }
    });
});
