#!/usr/bin/node

/**
 * Converts a number from base 10 to another base.
 * @param {number} base - The base to convert the number to.
 * @returns {function} - A function that converts a given number to the specified base.
 */
exports.converter = function (base) {
  /**
   * Converts a number to the specified base.
   * @param {number} number - The number to convert.
   * @returns {string} - The converted number as a string in the specified base.
   */
  return function (number) {
    return number.toString(base);
  };
};
