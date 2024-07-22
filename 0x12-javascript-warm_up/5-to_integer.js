#!/usr/bin/node
// Check if the second command line argument is not a number or if it's undefined
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
        // Not a number or argument not provided, print a message
          console.log('Not a number');
} else {
        // Argument is a number, print "My number:" followed by the integer value of the argument
          console.log('My number:', parseInt(process.argv[2]));
