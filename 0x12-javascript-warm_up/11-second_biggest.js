#!/usr/bin/node

const { argv } = require('node:process');

let argArray = argv.slice(2,);
let largest;
let secLargest;
if (argv[2] === undefined || argv.length === 3) {
  console.log(0);
} else {
  argArray.sort();
  largest = Math.max(...argArray);
  secLargest = argArray[argArray.length - 3, argArray.length-2];
}

console.log(secLargest);
