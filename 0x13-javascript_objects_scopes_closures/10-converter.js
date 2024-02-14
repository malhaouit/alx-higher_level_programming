#!/usr/bin/node

exports.converter = function (base) {
  return function (x) {
    if (base === 16) {
      return x.toString(16);
    } else if (base === 2) {
      return x.toString(2);
    }
    return x;
  };
};
