#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 5) {
  console.error('Usage: ./102-concat.js fileA fileB fileC');
  process.exit(1);
}

const [, , fileA, fileB, fileC] = process.argv;

// Read file A
fs.readFile(fileA, 'utf8', (err, dataA) => {
  if (err) {
    console.error(`Error reading ${fileA}:`, err);
    process.exit(1);
  }

  // Read file B
  fs.readFile(fileB, 'utf8', (err, dataB) => {
    if (err) {
      console.error(`Error reading ${fileB}:`, err);
      process.exit(1);
    }

    // Concatenate contents of fileA and fileB
    const concatenatedContent = `${dataA.trim()}\n${dataB.trim()}\n`;

    // Write to file C
    fs.writeFile(fileC, concatenatedContent, 'utf8', (err) => {
      if (err) {
        console.error(`Error writing to ${fileC}:`, err);
        process.exit(1);
      }

      console.log(`Concatenation of ${fileA} and ${fileB} saved to ${fileC}`);
    });
  });
});
