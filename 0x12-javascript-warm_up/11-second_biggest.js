#!/usr/bin/node

const argv = process.argv;

let secLargest;
if (argv[2] === undefined || argv.length === 3) {
  console.log(0);
} else {
  const argArray = argv
    .map(Number)
    .slice(2, argv.length)
    .sort((a, b) => a - b);
  secLargest = argArray[argArray.length - 2];
  console.log(secLargest);
}
