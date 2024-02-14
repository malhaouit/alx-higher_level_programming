#!/usr/bin/node

exports.converter = function (base) {
  return function (x) {
    if (base === 16) {
      return x.toString(16);
    }
    return x;
  };
};
