#!/usr/bin/node
const request = require('request');
const filmId = process.argv[2];
const filmUrl = 'https://swapi-api.alx-tools.com/api/films/';

request(filmUrl, (err, res, body) => {
  if (err) return;

  const films = JSON.parse(body).results;
  const film = films.find(film => film.url.endsWith(`/${filmId}/`));
  film.characters.forEach(characterUrl => {
    request(characterUrl, (err, res, body) => {
      if (err) return;
      console.log(JSON.parse(body).name);
    });
  });
});
