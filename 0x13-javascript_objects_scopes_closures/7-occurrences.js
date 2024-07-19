#!/usr/bin/node

/**
 * Counts the number of occurrences of searchElement in list.
 * @param {Array} list - The array in which to count occurrences.
 * @param {*} searchElement - The element to count occurrences of.
 * @returns {number} The number of occurrences of searchElement in list.
 */
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      count++;
    }
  }
  return count;
};
