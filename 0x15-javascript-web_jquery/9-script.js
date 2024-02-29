// Fetches the translation of "hello" from the given URL and displays it in the HTML tag DIV#hello

$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data) {
    $('#hello').text(data.hello);
});
