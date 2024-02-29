// Fetches and lists the titles for all movies from the given URL and adds them to the UL#list_movies tag

$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
    $.each(data.results, function(index, movie) {
        $('#list_movies').append('<li>' + movie.title + '</li>');
    });
});

