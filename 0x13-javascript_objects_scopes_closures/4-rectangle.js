#!/usr/bin/node

/**
 * Represents a rectangle.
 */
class Rectangle {
  constructor(w, h) {
    if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) {
      // Create an empty object if width or height is invalid
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

  /**
   * Exchanges the width and height of the rectangle.
   */
  rotate() {
    if (!this.width || !this.height) return; // Return if width or height is undefined

    [this.width, this.height] = [this.height, this.width];
  }

  /**
   * Doubles the width and height of the rectangle.
   */
  double() {
    if (!this.width || !this.height) return; // Return if width or height is undefined

    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
