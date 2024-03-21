#!/usr/bin/node

class Rectangle {
	/*
	 * Constructor function for creating instances of Rectangle
	 * Checking if both width and height are greater than 0
	 */
	constructor (w, h) {
		if ((w > 0) && (h > 0)) {
			this.width = w;
			this.height = h;
		}
	}
	print () {
		for (let i = 0; i < this.height; i++) {
			let s = '';
			for (let j = 0; j < this.width; j++) {
				s += 'X';
			}
			console.log(s);
		}
	}
	rotate () {
		const aux = this.width;
		this.width = this.height;
		this.height = aux;
	}
	double () {
		this.width *= 2;
		this.height *= 2;
	}
}
module.exports = Rectangle; // Exporting the Rectangle class for use in other modules
