#!/usr/bin/node

// Check if the command line argument is missing or not a number
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
         // Print a message indicating missing size
          console.log('Missing size');
} else {
         // Convert the command line argument to a number
          const x = Number(process.argv[2]);
          let i = 0;
        // Use a while loop to print a string of 'X' characters repeated horizontally x times
          while (i < x) {
                   // Print the message with 'X' characters repeated x times
                      console.log('X'.repeat(x));
                      i++;
                  //Increament counter
                    }
