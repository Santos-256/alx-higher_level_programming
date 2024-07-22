#!/usr/bin/node
// Check if the second command line argument is undefined
if (process.argv[2] === undefined) {
        // No argument provided, print a message
          console.log('No argument');
} else {
         // Argument found, print the value of the argument
          console.log(process.argv[2]);
}
