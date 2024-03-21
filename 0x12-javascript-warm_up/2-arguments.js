#!/usr/bin/node
// Check the number of command line arguments
if (process.argv.length === 2) {
	// No arguments provided
	  console.log('No argument');
}
else if (process.argv.length === 3) {
	// One argument provided
	  console.log('Argument found');
}
else {
	// More than one argument provided
	  console.log('Arguments found');
}
