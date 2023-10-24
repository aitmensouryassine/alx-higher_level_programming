#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (err, res, body) => {
  if (!err) {
    const films = JSON.parse(body).results;
    const characterFilms = films.filter(({ characters }) => characters.find(char => char.endsWith('/18/')));
    console.log(characterFilms.length);
  }
});
