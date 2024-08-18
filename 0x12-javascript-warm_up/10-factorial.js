#!/usr/bin/node
const num = parseInt(process.argv[2]);
function factorial (x) {
  if (x > 0) { return (x * factorial(x - 1)); }
  return 1;
}
console.log(factorial(num));
