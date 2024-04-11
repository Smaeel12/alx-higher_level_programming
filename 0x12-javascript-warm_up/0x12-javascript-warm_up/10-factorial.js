#!/usr/bin/node

let res = 1;
function factorial (n) {
  if (n <= 0 || isNaN(n)) {
    return res;
  }
  res *= n;
  return factorial(--n);
}
console.log(factorial(Number(process.argv[2])));
