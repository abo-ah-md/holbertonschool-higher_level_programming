#!/usr/bin/node
const { argv } = require('process');

if (argv[2] === 1) {
  console.log(NaN);
  
}
function recursiveFactorial (num) {
  if (num === 1) {
    return num;
  }
  return num * recursiveFactorial(num - 1);
}

const number = recursiveFactorial(Number(argv[2]));
console.log(number);
