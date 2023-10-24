#!/usr/bin/node
const request = require('request');
const episode = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${episode}`;

request(url, (err, res, body) => {
  if (err) { return; }
  console.log(JSON.parse(body).title);
});
