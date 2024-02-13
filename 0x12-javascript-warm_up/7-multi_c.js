#!/usr/bin/node
const argument = process.argv[2];
const converted = parseInt(argument);
if (isNaN(converted)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < converted; i++) {
    console.log('C is fun');
  }
}
