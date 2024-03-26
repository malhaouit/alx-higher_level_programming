#!/usr/bin/node

const request = require('request');
const args = process.argv;
const URL = args[2];
request
  .get(URL)
  .on('response', function (response) {
    console.log(`code: ${response.statusCode}`);
  });
