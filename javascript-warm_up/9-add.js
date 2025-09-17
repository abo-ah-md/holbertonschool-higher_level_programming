#!/usr/bin/node
const { argv } = require('process');

function add(a, b){
  if (Number(a) && Number(b)) {
console.log(`${Number(a) + Number(b)}`);
} 
}

add(argv[2],argv[3]);


