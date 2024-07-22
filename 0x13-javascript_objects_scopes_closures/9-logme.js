#!/usr/bin/node // Shebang line specifying the interpreter to use (Node.js)
let narg = 0;

exports.logMe = function (item) {
        /*
         *  Exporting a function named logMe
         *  The function takes one parameter: item (the item to be logged)
         */
          console.log(narg + ': ' + item);
          narg++;
};
