#!/usr/bin/node //shebang saticifying the interpreter to use (Node.js)

exports.nbOccurences = function (list, searchElement) {
	 // Exporting a function named nbOccurences
	// The function takes two parameters: list (the array to search in) and searchElement (the element to count occurrences of)
	let nOccurrences = 0;
	for (let i = 0; i < list.length; i++) {
		if (searchElement === list[i]) {
			nOccurrences++;
		}
	}
	return nOccurrences;
};
