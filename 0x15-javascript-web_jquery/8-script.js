//  fetches and lists all movies title by using this URL: https://swapi.co/api/films/?format=json

const url = 'https://swapi.co/api/films/?format=json';
$.get(url, function (data) {
  for (let j = 0; j < data.count; j++) {
    $('UL#list_movies').append('<li>' + data.results[j].title + '</li>');
  }
});
