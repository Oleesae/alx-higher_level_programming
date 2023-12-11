#!/usr/bin/node

const { argv } = require('node:process');

// Adds two integers
function add (a, b) {
  return (parseInt(a) + parseInt(b));
}

console.log(add(argv[2], argv[3]));
