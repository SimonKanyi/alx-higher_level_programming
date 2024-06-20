#!/usr/bin/node

/**
 * Represents a rectangle.
 */
class Rectangle {
  constructor(w, h) {
    // Check if either width or height is not a positive integer or is 0
    if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) {
      // Create an empty object
      return {};
    } else {
      // Initialize width and height attributes
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
