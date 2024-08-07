$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    // Iterate over the movies array and append each title to the list
    data.results.forEach(function (film) {
      $('#list_movies').append('<li>' + film.title + '</li>');
    });
  });
});
