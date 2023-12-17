#!/usr/bin/node

function esrever (list) {
  const reversed = [];
  let i = 0;
  while (reversed.length !== list.length) {
    reversed[i] = list[list.length - i - 1];
    i++;
  }
  return reversed;
}

exports.esrever = esrever;
