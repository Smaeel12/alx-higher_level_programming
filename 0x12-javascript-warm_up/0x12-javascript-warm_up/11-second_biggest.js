#!/usr/bin/node

let num1 = 0; let num2 = 0;
for (const n of process.argv.slice(2)) {
  if (num1 < n) {
    num2 = num1;
    num1 = n;
  }
}
console.log(num2);
