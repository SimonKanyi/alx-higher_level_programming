#!/usr/bin/node

const fs = require('fs');

// Get the file path and string to write from the command line arguments
const filePath = process.argv[2];
const stringToWrite = process.argv[3];

fs.writeFile(filePath, stringToWrite, 'utf8', (err) => {
  if (err) {
    // Print the error object if there's an issue with writing to the file
    console.log(err);
  }
});
