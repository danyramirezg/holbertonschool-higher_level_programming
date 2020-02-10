#!/usr/bin/node
// Class Rectangle that defines a rectangle. The constructor take 2 arguments w and h. If w or h is equal to 0 or not a positive integer, create an empty object

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
      return this;
    } else {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
