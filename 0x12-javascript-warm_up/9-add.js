#!/usr/bin/node
const args = process.argv.slice(2);
const arg1 = parseInt(args[0]);
const arg2 = parseInt(args[1]);
function add (a, b) {
  return a + b;
}
console.log(add(arg1, arg2));
