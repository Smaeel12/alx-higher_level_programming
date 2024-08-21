#!/usr/bin/node
const request = require('request');

request.get(process.argv[2], function (err, response, body) {
  err && console.log(err);
  let count = 0;
  for (const film of JSON.parse(body).results) {
    film.characters.forEach(element => {
      if (element.includes('/18/')) count++;
    });
  }
  console.log(count);
});