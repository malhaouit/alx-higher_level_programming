#!/usr/bin/node

const fs = require('fs');
const args = process.argv;
const filename = args[2];
fs.readFile(filename, 'utf8', (err, content) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(content);
});
