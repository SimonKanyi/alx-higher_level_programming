#!/usr/bin/node

/**
 * Reverses a given list without using the built-in reverse method.
 * @param {Array} list - The array to be reversed.
 * @returns {Array} The reversed version of the list.
 */
exports.esrever = function (list) {
  let reversed = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reversed.push(list[i]);
  }
  return reversed;
};
