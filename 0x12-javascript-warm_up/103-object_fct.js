#!/usr/bin/node
// Shebang: Specifies the interpreter to be used when running the script, in this case, Node.js.
const myObject = {
	  type: 'object',
	  value: 12
};
console.log(myObject);
myObject.incr = function () {
	  this.value++;
};
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
