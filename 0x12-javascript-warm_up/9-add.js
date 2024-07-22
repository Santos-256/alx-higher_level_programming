#!/usr/bin/node

// Define a function called 'add' that takes two parameters (a and b)
function add (a, b) {
         // Calculate the sum of a and b
          const c = a + b;
         // Print the result to the console
          console.log(c);
}
// Call the 'add' function with two command line arguments converted to numbers
add(Number(process.argv[2]), Number(process.argv[3]));
