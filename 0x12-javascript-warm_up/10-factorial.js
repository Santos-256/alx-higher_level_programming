#!/usr/bin/node

// Shebang: Specifies the interpreter to be used when running the script, in this case, Node.js.
function factorial (n) {
        //Function to calculate the factorial of a given number 'n'.
          if (n < 0) {
                      return (-1);
                    }
          if (n === 0 || isNaN(n)) {
                      return (1);
                    }
          return (n * factorial(n - 1));
}

console.log(factorial(Number(process.argv[2])));
