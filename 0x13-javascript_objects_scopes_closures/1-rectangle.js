#!/usr/bin/node // Shebang line specifying the interpreter to use (Node.js)

class Rectangle {
	 // Constructor function for creating instances of Rectangle
	  constructor (w, h) {
		      this.width = w;
		      this.height = h;
		    }
}

 // Exporting the Rectangle class for use in other modules
module.exports = Rectangle;
