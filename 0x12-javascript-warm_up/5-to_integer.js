#!/usr/bin/node
const argument = process.argv[2];
const converted = parseInt(argument);
if (isNaN(converted)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + converted);
}
