#!/usr/bin/node // Shebang line specifying the interpreter to use (Node.js)

class Rectangle {
        /* Constructor function for creating instances of Rectangle
         * and
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

module.exports = Rectangle; // Exporting the Rectangle class for use in other modules
