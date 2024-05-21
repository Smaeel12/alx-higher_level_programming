#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const film = JSON.parse(body);
    const charactersUrls = film.characters;
    printCharactersInOrder(charactersUrls);
  }
});

function printCharactersInOrder (charactersUrls) {
  let count = 0;
  charactersUrls.forEach(characterUrl => {
    request(characterUrl, (err, resp, characterBody) => {
      if (err) {
        console.error(err);
      } else {
        const character = JSON.parse(characterBody);
        console.log(character.name);
        count++;
        if (count === charactersUrls.length) {
          console.log('All characters printed.');
        }
      }
    });
  });
}
