#!/usr/bin/node
// Importing the 'dict' object from the '101-data.js' file
const dict = require('./101-data').dict;
// Convert the 'dict' object into an array of key-value pairs
const totalist = Object.entries(dict);
// Extract just the values from the original dictionary
const vals = Object.values(dict);
const valsUniq = [...new Set(vals)];
const newDict = {};

// Loop through the unique values
for (const j in valsUniq) {
	  const list = [];
	  for (const k in totalist) {
		      if (totalist[k][1] === valsUniq[j]) {
			            list.unshift(totalist[k][0]);
			          }
		    }
	 // Assign the list array to the current unique value in the new dictionary
	  newDict[valsUniq[j]] = list;
}
console.log(newDict);
