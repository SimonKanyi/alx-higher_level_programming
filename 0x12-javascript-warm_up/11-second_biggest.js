#!/usr/bin/node

function secondBiggest(args) {
    // If no arguments or only one argument, return 0
    if (args.length <= 1) {
        return 0;
    }
    
    // Convert arguments to integers and sort them in descending order
    const numbers = args.map(arg => parseInt(arg));
    const sortedNumbers = numbers.sort((a, b) => b - a);
    
    // Return the second element in the sorted array
    return sortedNumbers[1];
}

const args = process.argv.slice(2); // Remove first two elements (node and script name)
console.log(secondBiggest(args));
