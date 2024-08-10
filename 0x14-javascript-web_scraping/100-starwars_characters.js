#!/usr/bin/node

const request = require('request');

// Get the Movie ID from the command line argument
const movieId = process.argv[2];

// Construct the URL to get the movie details
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Function to print character names
const printCharacterNames = (characters) => {
  characters.forEach(url => {
    request(url, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }

      try {
        const character = JSON.parse(body);
        console.log(character.name);
      } catch (e) {
        console.error(e);
      }
    });
  });
};

// Fetch movie details
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  try {
    const movie = JSON.parse(body);
    const characterUrls = movie.characters;
    
    printCharacterNames(characterUrls);
  } catch (e) {
    console.error(e);
  }
});
