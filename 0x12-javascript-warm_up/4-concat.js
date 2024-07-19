#!/usr/bin/node

const arg1 = process.argv[2] || 'undefined'; // process.argv[2] is the first argument, default to 'undefined' if not provided
const arg2 = process.argv[3] || 'undefined'; // process.argv[3] is the second argument, default to 'undefined' if not provided

console.log(`${arg1} is ${arg2}`);
