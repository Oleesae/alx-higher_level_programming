#!/usr/bin/node

const Rectangle = require('./5-square.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let square = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        if (c === undefined) {
          square += 'X';
        } else {
          square += c;
        }
      }
      if (i < this.height - 1) square += '\n';
    }
    console.log(square);
  }
}

module.exports = Square;
