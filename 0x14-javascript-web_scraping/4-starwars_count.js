#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];
const characterId = 18;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(body).results;
    const count = films.reduce((acc, film) => {
      const characterPresent = film.characters.some(characterUrl => characterUrl.includes(`/18/`));
      return acc + (characterPresent ? 1 : 0);
    }, 0);
    console.log(count);
  }
});
