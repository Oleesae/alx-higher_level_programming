#!/usr/bin/node

const { argv } = require('node:process');

// Computes the factorial of a number
function factorial (n) {
  if (n <= 1) {
    return (1);
  } else {
    return n * factorial(n - 1);
  }
}

if (argv[2] === undefined) {
  console.log(1);
} else {
  console.log(factorial(parseInt(argv[2])));
}
