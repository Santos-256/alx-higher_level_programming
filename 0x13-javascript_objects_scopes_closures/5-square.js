#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
          constructor (size) {
                  // Constructor function for creating instances of Square
                 // Calling the constructor of the Rectangle class with the same size for width and height
                      super(size, size);
                    }
}

module.exports = Square;// Exporting the Square class for use in other modules
