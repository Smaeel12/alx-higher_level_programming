#!/usr/bin/node
const Sqr = require('./5-square');

class Square extends Sqr {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    const char = (c || 'X');
    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.width));
    }
  }
}

module.exports = Square;
