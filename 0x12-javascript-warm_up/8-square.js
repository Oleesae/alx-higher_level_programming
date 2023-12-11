#!/usr/bin/node

const argv = process.argv;

let msg = '';
if (isNaN(argv[2]) || argv[2] === undefined) {
  msg += 'Missing size';
} else {
  if (parseInt(argv[2]) >= 1) {
    for (let i = 0; i < argv[2]; i++) {
      let j = 0;
      while (j < argv[2]) {
        msg += 'X';
        j++;
      }
      if (i !== argv[2] - 1) msg += '\n';
    }
  }
}

console.log(msg);
