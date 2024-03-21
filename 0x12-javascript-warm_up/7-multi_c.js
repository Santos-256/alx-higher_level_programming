#!/usr/bin/node
// Check if the command line argument is missing or not a number
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
	// Print a message indicating missing number of occurrences
	  console.log('Missing number of occurrences');
} else {
	// Convert the command line argument to a number
	  const x = Number(process.argv[2]);
	  let i = 0;
	// Use a while loop to print 'C is fun' x times
	  while (i < x) {
		  //print the messege
		      console.log('C is fun');
		      i++;
		    }
}
