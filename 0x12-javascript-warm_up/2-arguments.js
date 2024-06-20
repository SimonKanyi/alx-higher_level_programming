#!/usr/bin/node

const args = process.argv.slice(2); // process.argv includes 'node' and the script path, so slice to get only arguments

if (args.length === 0) {
    console.log("No argument");
} else if (args.length === 1) {
    console.log("Argument found");
} else {
    console.log("Arguments found");
}
