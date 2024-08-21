#!/usr/bin/node
const request = require('request');

request.get('https://swapi-api.alx-tools.com/api/films/', function (err, response, body) {
  err && console.log(err);
  let count = 0;
  for (const film of JSON.parse(body).results) {
    if (film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      count++;
    }
  }
  console.log(count);
});
