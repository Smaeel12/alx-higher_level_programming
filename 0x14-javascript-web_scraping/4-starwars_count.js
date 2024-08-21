#!/usr/bin/node
// makes get request for SW movie id
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) throw new Error(error);
  let count = 0;
  for (const film of JSON.parse(body).results) {
    for (const character of film.characters) {
      if (character.includes('/18/')) count++;
    }
  }
  console.log(count);
});