#!/usr/bin/node
// Importing the 'list' array from the '100-data.js' file
const list = require('./100-data.js').list;
// Printing the original 'list' array
console.log(list);
// Mapping over the elements of the 'list' array and multiplying each element by its index
console.log(list.map((item, index) => item * index));
