#!/usr/bin/node

const argv = process.argv;
let msg = '';

if (argv.length < 3) {
  msg += 'No argument';
} else if (argv.length > 3) {
  msg += 'Arguments found';
} else {
  msg += 'Argument found';
}

console.log(msg);
