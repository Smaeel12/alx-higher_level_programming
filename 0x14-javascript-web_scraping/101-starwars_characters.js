#!/usr/bin/node

const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Construct the API URL for the specified movie ID
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Make a GET request to the Star Wars API endpoint for the specified movie ID
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    // Parse the response body
    const film = JSON.parse(body);
    // Extract the characters' URLs in the same order as they appear in the /films/ response
    const charactersUrls = film.characters;

    // Function to print characters' names in the correct order
    printCharactersInOrder(charactersUrls);
  }
});

// Function to print characters' names in the correct order
function printCharactersInOrder(charactersUrls) {
  // Iterate over the character URLs and make individual requests to get each character's details
  charactersUrls.forEach(characterUrl => {
    // Make a GET request to the character URL
    request(characterUrl, (err, resp, characterBody) => {
      if (err) {
        console.error(err);
      } else {
        // Parse the response body to extract character details
        const character = JSON.parse(characterBody);
        // Print the character's name
        console.log(character.name);
      }
    });
  });
}
