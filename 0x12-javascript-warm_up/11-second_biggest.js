#!/usr/bin/node
console.log(process.argv.length > 3 ? process.argv.slice(2).sort((a, b) => b - a)[1] : 0);
// console.log(process.argv.length >= 4 ? process.argv.sort()[process.argv.length - 2] : 0)
