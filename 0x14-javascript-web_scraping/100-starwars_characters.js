#!/usr/bin/node
const request = require('request');

request.get(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, function (err, response, body) {
  if (err) throw new Error(err);
  JSON.parse(body).characters.forEach(character => {
    request(character, (err, res, body) => {
      if (err) throw new Error(err);
      console.log(JSON.parse(body).name);
    });
  });
});
