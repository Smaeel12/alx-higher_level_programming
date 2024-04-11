#!/usr/bin/node

const narg = process.argv.length - 2; // number of args
// options
if (narg === 0) {
  console.log('No Argument');
} else if (narg === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
