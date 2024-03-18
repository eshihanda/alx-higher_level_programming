#!/usr/bin/node
exports.esrever = function (list) {
  const listcpy = list.slice();
  let i = 0;
  for (i = 0; i < list.length; i++) {
    list[i] = listcpy[list.length - i - 1];
  }
  return list;
};
