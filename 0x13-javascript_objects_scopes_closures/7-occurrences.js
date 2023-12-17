#!/usr/bin/node

function nbOccurences (list, searchElement) {
  const total = list.filter(item => item === searchElement);
  return total.length;
}

exports.nbOccurences = nbOccurences;
