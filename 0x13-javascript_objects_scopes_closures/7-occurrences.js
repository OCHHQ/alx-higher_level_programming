#!/usr/bin/node

module.exports = class Square {
  constructor (size) {
    this.size = size;
  }

  print () {
    for (let i = 0; i < this.size; i++) {
      console.log('X'.repeat(this.size));
    }
  }
};
