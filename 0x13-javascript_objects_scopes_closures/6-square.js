#!/usr/bin/node

const Rectangle = require('./5-square.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let square = '';
    for (let i = 0; i < this.size; i++) {
      for (let j = 0; j < this.size; j++) {
        if (c === undefined) {
          square += 'X';
        } else {
          square += c;
        }
      }
      if (i < this.size - 1) square += '\n';
    }
    console.log(square);
  }
}

module.exports = Square;
