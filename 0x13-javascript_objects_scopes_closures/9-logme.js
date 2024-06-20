#!/usr/bin/node

let count = 0;

/**
 * Prints the number of arguments already printed and the new argument value.
 * @param {*} item - The argument to be printed.
 */
exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count++;
};
