// Fetches the character name from the given URL and displays it in the div#character tag
$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(data) {
  $('div#character').text(data.name);
});
