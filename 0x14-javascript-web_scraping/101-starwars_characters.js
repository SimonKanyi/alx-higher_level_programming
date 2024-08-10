#!/usr/bin/node

const request = require('request');

// Get the Movie ID from the command line argument
const movieId = process.argv[2];

// Construct the URL to get the movie details
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Fetch movie details
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  try {
    const movie = JSON.parse(body);
    const characterUrls = movie.characters;

    // Function to fetch and print character names
    const printCharacterNames = (urls) => {
      let remaining = urls.length;
      urls.forEach(url => {
        request(url, (err, res, characterBody) => {
          if (err) {
            console.error(err);
            return;
          }

          try {
            const character = JSON.parse(characterBody);
            console.log(character.name);
          } catch (e) {
            console.error(e);
          }

          // Check if all character requests are done
          remaining--;
          if (remaining === 0) {
            process.exit();
          }
        });
      });
    };

    printCharacterNames(characterUrls);
  } catch (e) {
    console.error(e);
  }
});
