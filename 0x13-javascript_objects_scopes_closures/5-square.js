#!/usr/bin/node
const Rectangle = require('./4-rectangle');

/**
 * Represents a square, which is a special case of Rectangle.
 */
class Square extends Rectangle {
  constructor(size) {
    super(size, size); // Call the constructor of Rectangle with size as both width and height
  }
}

module.exports = Square;
