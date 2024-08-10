#!/usr/bin/node

const request = require('request');

// Get the API URL from the command line arguments
const apiUrl = process.argv[2];

// Character ID for Wedge Antilles
const wedgeAntillesId = '18';

// Make a GET request to the API URL
request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(body).results;
    let count = 0;

    // Loop through each film and check if Wedge Antilles is in the characters list
    for (const film of films) {
      if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeAntillesId}/`)) {
        count++;
      }
    }

    // Print the number of movies where Wedge Antilles is present
    console.log(count);
  }
});
