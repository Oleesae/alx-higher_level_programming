#!/usr/bin/node
const Rectangle = require('./4-rectangle');

const r1 = new Rectangle(2, 3);

r1.print();
console.log('Normal: ' + r1.width);


r1.double();
r1.print();
console.log('Double: ' + r1.width);


r1.rotate();
r1.print();
console.log('Rotate: ' + r1.width);
