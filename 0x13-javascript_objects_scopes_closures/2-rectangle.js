#!/usr/bin/node

class Rectangle {
	// Constructor function for creating instances of Rectangle
	  constructor (w, h) {
		  // Checking if both width and height are greater than 0
		      if ((w > 0) && (h > 0)) {
			            this.width = w; // Assigning the width property
			            this.height = h;  // Assigning the height property
			          }
		    }
}

module.exports = Rectangle; // Exporting the Rectangle class for use in other modules
