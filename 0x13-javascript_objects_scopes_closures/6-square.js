#!/usr/bin/node
const SquareP = require('./5-square');// Importing the Square class from the '5-square.js' file


class Square extends SquareP {
         // Extending the Square class from SquareP (SquareP is the parent class)
        charPrint (c) {
                 // Method to print the square using a specific character, defaulting to 'X'
                if (c === undefined) {
                        c = 'X';
                }
                for (let i = 0; i < this.height; i++) {
                        let s = '';
                        for (let j = 0; j < this.width; j++) {
                                s += c;
                        }
                        console.log(s);
                }
        }
}

module.exports = Square; // Exporting the Square class for use in other modules
