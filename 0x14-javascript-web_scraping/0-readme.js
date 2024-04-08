#!/usr/bin/node
// reads and prints the contents of a file
const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', function (error, content) {
  console.log(error || content);
});
