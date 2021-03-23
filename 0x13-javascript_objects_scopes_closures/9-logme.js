#!/usr/bin/node
let _count = 0;
exports.logMe = function (item) {
  console.log(_count + ': ' + item);
  _count++;
};
