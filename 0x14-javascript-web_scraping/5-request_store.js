#!/usr/bin/node
const fs = require('fs');
const request = require('request');

request.get(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]), 'utf-8');
