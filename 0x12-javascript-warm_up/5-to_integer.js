#!/usr/bin/node

const arg = process.argv[2]; // Get the first argument

if (!arg || isNaN(parseInt(arg))) {
    console.log("Not a number");
} else {
    const number = parseInt(arg); // Convert the argument to an integer
    console.log(`My number: ${number}`);
}
