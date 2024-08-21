#!/usr/bin/node
const request = require('request');

const dict = {};
let characters;
request.get(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, function (err, response, body) {
  if (err) throw new Error(err);
  characters = JSON.parse(body).characters;
  characters.forEach(character => {
    request(character, (err, res, body) => {
      if (err) throw new Error(err);
      add(JSON.parse(body).url, JSON.parse(body).name);
    });
  });
});

function add (url, name) {
  dict[url] = name;
  if (Object.entries(dict).length === characters.length) {
    for (url of characters) {
      console.log(dict[url]);
    }
  }
}
