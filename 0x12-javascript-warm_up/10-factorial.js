#!/usr/bin/node

function factorial(n) {
    // Base case: factorial of NaN or non-positive number is 1
    if (isNaN(parseInt(n)) || parseInt(n) <= 0) {
        return 1;
    }
    // Recursive case: calculate factorial
    return parseInt(n) * factorial(parseInt(n) - 1);
}

const num = process.argv[2];
console.log(factorial(num));
