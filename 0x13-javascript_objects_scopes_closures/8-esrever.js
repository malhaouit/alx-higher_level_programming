#!/usr/bin/node

exports.esrever = function (list) {
  const length = list.length;
  let j = length - 1;
  for (let i = 0; i < length / 2; i++) {
    const temp = list[i];
    list[i] = list[j];
    list[j] = temp;
    j--;
  }
  return list;
};
