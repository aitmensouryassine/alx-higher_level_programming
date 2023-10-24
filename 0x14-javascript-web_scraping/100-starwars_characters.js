#!/usr/bin/node
const request = require('request');
const filmId = process.argv[2];
const filmUrl = `https://swapi-api.alx-tools.com/api/films/${filmId}`;

request(filmUrl, (err, res, body) => {
  if (err) return;

  const characters = JSON.parse(body).characters;
  characters.forEach(characterUrl => {
    request(characterUrl, (err, res, body) => {
      if (err) return;
      console.log(JSON.parse(body).name);
    });
  });
});
