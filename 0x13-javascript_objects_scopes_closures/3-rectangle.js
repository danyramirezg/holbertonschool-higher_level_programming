#!/usr/bin/node
// Class Rectangle. Create an instance method called print() that prints the rectangle using the character X

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
      return this;
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let rows = 0; rows < this.height; rows++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
