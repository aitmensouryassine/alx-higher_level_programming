#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const characterUrl = 'https://swapi-api.alx-tools.com/api/people/18/';

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const films = JSON.parse(body).results;
  const characterFilms = films
    .filter(({ characters }) => characters.includes(characterUrl));
  console.log(characterFilms.length);
});
