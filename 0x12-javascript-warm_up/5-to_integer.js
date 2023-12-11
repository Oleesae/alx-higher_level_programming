#!/usr/bin/node

const { argv } = require('node:process');

let msg = '';
if (isNaN(argv[2])) {
  msg += 'Not a number';
} else {
  msg += 'My number: ' + parseInt(argv[2]);
}

console.log(msg);
