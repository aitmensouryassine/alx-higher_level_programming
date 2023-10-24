#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const path = process.argv[3];
const fs = require('fs');

request(url, (err, res, body) => {
  if (err) return;

  fs.writeFile(path, body, { encoding: 'utf-8' }, (err) => {
    if (err) {
      console.log(err);
    }
  });
});
