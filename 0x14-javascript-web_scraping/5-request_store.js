#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const args = process.argv;
const requestURL = args[2];
const fileToWrite = args[3];

request(requestURL).pipe(fs.createWriteStream(fileToWrite));
