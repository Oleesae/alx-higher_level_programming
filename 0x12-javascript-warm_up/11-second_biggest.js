#!/usr/bin/node

const argv = process.argv;

const argArray = argv.slice(2, argv.length);
let secLargest;
if (argv[2] === undefined || argv.length === 3) {
  console.log(0);
} else {
  argArray.sort();
  secLargest = argArray[argArray.length - 2];
}

console.log(secLargest);
