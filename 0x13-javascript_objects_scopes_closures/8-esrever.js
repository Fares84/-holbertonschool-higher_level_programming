#!/usr/bin/node
exports.esrever = function (list) {
  const _reverse = [];
  for (let i = list.length - 1; i >= 0; i--) {
    _reverse.push(list[i]);
  }
  return _reverse;
};
