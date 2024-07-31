#!/usr/bin/node

const request = require('request');

const apiUrl = 'https://swapi-api.alx-tools.com/api/films/';
const characterId = 18;
let movieCount = 0;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  const movies = JSON.parse(body).results;
  movies.forEach((movie) => {
    movie.characters.forEach((character) => {
      if (character.endsWith(`/${characterId}/`)) {
        movieCount++;
      }
    });
  });
  console.log(movieCount);
});
