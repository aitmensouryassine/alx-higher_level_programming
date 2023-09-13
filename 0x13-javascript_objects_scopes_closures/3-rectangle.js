#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let l = 0; l < this.height; l++) {
      let row = '';
      for (let c = 0; c < this.width; c++) row += 'X';
      console.log(row);
    }
  }
};
