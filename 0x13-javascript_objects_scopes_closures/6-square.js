#!/usr/bin/node
module.exports = class Square extends require('./5-square') {
  charPrint (c) {
    if (c === undefined) this.print();
    else {
      for (let row = 0; row < this.height; row++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
