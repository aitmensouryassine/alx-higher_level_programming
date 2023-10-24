#!/usr/bin/node
const request = require('request');
const filmId = process.argv[2];
const filmUrl = 'https://swapi-api.alx-tools.com/api/films/';

function asyncRequest (url) {
  return new Promise(function (resolve, reject) {
    request(url, function (error, res, body) {
      if (error) {
        reject(error);
      }
      resolve(JSON.parse(body));
    });
  });
}

request(filmUrl, async (err, res, body) => {
  if (err) return;
  const films = JSON.parse(body).results;
  const film = films.find(film => film.url.endsWith(`/${filmId}/`));

  let requests = [];
  film.characters.forEach((characterUrl) => {
    requests.push(asyncRequest(characterUrl));
  });
  requests = await Promise.all(requests);

  requests.forEach(character => console.log(character.name));
});
