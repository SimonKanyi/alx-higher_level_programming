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

  /**
   * Prints the rectangle using 'X' characters.
   */
  print() {
    if (!this.width || !this.height) return; // Return if width or height is undefined

    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }
}

module.exports = Rectangle;
