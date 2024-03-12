#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
	// Exports a function named 'callMeMoby' that takes two parameters: 'x' and 'theFunction'.
	  for (let i = 0; i < x; i++) {
		      // Executes 'theFunction' 'x' times in a loop.
		      theFunction();
		    }
};
//The module exports the 'callMeMoby' function, making it accessible for use in other modules.
