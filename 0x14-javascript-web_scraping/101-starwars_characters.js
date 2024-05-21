#!/usr/bin/node

const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Construct the API URL for the specified movie ID
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Function to make a request and retrieve character name
const getCharacterName = async (characterUrl) => {
  return new Promise((resolve, reject) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const character = JSON.parse(body);
        resolve(character.name);
      }
    });
  });
};

// Main function to retrieve characters and print their names
const main = async () => {
  try {
    const response = await new Promise((resolve, reject) => {
      request(apiUrl, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          resolve(body);
        }
      });
    });

    const film = JSON.parse(response);
    const charactersUrls = film.characters;

    // Retrieve character names asynchronously and print them in order
    for (const characterUrl of charactersUrls) {
      const characterName = await getCharacterName(characterUrl);
      console.log(characterName);
    }
  } catch (error) {
    console.error('Error:', error);
  }
};

// Call the main function
main();

