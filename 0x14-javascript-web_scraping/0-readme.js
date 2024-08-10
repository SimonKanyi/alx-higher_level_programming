#!/usr/bin/node

const fs = require('fs');

// Get the file path from the command line arguments
const filePath = process.argv[2];

fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    // Print the error object if there's an issue with reading the file
    console.log(err);
  } else {
    // Print the content of the file
    console.log(data);
  }
});
