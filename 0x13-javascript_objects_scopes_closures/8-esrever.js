#!/usr/bin/node

exports.esrever = function (list) {
  // Use a loop to reverse the array without using the reverse method
  const reversed = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reversed.push(list[i]);
  }
  return reversed;
};
