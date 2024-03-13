#!/usr/bin/node

const Square1 = require('./5-square');
module.exports = class Square extends Square1 {
  constructor (size = 0) {
    super(size);
  }

  charPrint (c) {
    if (typeof c === 'undefined') {
      this.print();
    } else {
      let string = '';
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          string += c;
        }
        console.log(string);
        string = '';
      }
    }
  }
}
