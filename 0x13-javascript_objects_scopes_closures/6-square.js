#!/usr/bin/node

const Square_1 = require('./5-square');
class Square extends Square_1 {
	constructor (size) {
		super (size);
	}
	charPrint (c) {
		if (c) {
			for (let i = 0; i < this.height; i++) {
				console.log(c.repeat(this.width));
			}
		} else {
			this.print()
		}
	}
}

module.exports = Square;
