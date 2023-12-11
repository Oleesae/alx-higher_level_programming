#!/usr/bin/node

const argv = process.argv;
let msg = '';

if (argv[2] === undefined) {
  msg += 'No argument';
} else {
  msg += `${argv[2]}`;
}

console.log(msg);
