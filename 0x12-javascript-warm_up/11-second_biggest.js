#!/usr/bin/node
if (process.argv.length <= 3) {
	// Checks if the number of command-line arguments is less than or equal to 3.
	  console.log('0');
} else {
	 // Extracts command-line arguments starting from index 2, converts them to numbers, and stores them in an array 'arr'.
	  const arr = process.argv.slice(2).map(Number);

	// Sorts the array in descending order and retrieves the second element (index 1) which is the second largest value.
	  const second = arr.sort(function (a, b) { return b - a; })[1];
	  console.log(second);
}
