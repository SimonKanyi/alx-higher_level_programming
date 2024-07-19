#!/usr/bin/node
const SquareBase = require('./5-square');

/**
 * Represents a square, inherits from SquareBase (5-square.js).
 */
class Square extends SquareBase {
  constructor(size) {
    super(size); // Call the constructor of SquareBase with size
  }

  /**
   * Prints the square using the character c.
   * If c is undefined, use 'X'.
   * @param {string} c - The character to use for printing.
   */
  charPrint(c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.size; i++) {
      console.log(c.repeat(this.size));
    }
  }
}

module.exports = Square;
