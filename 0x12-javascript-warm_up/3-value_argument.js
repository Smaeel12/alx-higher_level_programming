#!/usr/bin/env node

const arg = process.argv[2];
if (arg !== undefined) {
  console.log(arg);
} else {
  console.log('No argument');
}
