#!/usr/bin/node

const fs = require('fs');
const args = process.argv;
const fileName = args[2];
const stringToWrite = args[3];

fs.writeFile(fileName, stringToWrite, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
