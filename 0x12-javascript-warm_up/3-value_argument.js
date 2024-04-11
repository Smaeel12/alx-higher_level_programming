#!/usr/bin/node

const farg = process.argv[2];
if (farg !== undefined) {
  console.log(farg);
} else {
  console.log('No argument');
}
