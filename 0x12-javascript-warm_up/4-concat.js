#!/usr/bin/node

const { argv } = require('node:process');

const msg = `${argv[2]} is ${argv[3]}`;

console.log(msg);
