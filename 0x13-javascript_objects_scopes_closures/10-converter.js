#!/usr/bin/node // Shebang line specifying the interpreter to use (Node.js)

exports.converter = function (base) {
	/*
	 *  Exporting a function named converter
	 *  The function takes one parameter: base (the base to which numbers will be converted)
	 */
	return function (num) {
		return num.toString(base);
	};
};
