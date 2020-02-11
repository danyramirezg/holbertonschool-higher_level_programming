#!/usr/bin/node
// class Square that defines a square and inherits from Square of 5-square.js

const Square1 = require('./5-square');

class Square extends Square1 {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let rows = 0; rows < this.height; rows++) {
        console.log(c.repeat(this.height));
      }
    }
  }
}

module.exports = Square;
