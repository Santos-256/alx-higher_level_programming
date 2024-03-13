#!/usr/bin/node
// The shebang line indicates that the script should be executed using Node.js.
const fs = require('fs');
// Importing the Node.js 'fs' (file system) module to perform file operations.

const fArg = fs.readFileSync(process.argv[2]).toString();
// Reading the contents of the first file specified as a command-line argument and converting it to a string.
const sArg = fs.readFileSync(process.argv[3]).toString();
// Reading the contents of the second file specified as a command-line argument and converting it to a string.
fs.writeFileSync(process.argv[4], fArg + sArg);
// Writing the concatenated contents of the two files to the third file specified as a command-line argument.
