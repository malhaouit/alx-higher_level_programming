#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  let numOccurences = 0;
  while (i < list.length) {
    if (list[i] === searchElement) {
      numOccurences++;
    }
    i++;
  }
  return numOccurences;
};
