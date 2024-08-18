#!/usr/bin/node
const x = Number(process.argv[2]);
if (x) {
  for (let a = 0; a < x; a++) {
    console.log('X'.repeat(x));
  }
}
