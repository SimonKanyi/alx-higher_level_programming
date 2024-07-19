#!/usr/bin/node

const arg = process.argv[2]; // process.argv includes 'node' and the script path, so access index 2 for the first argument

if (!arg) {
    console.log("No argument");
} else {
    console.log(arg);
}
