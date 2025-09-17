#!/usr/bin/node
const { argv } = require('process');
if (argv[2] === null) {
  console.log('No argument');
} else {
  const args = argv.slice(2);
  args.forEach((value, index) => console.log(value));
}
