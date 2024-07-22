#!/usr/bin/node
const myObject = {
          type: 'object',
          value: 12
};

// Creates an object 'myObject' with properties 'type' and 'value' initialized to 'object' and 12, respectively.
console.log(myObject);
// Prints the initial state of 'myObject' to the console.
myObject.value = 89;
console.log(myObject);
