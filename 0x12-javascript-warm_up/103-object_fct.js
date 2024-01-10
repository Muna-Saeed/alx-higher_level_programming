#!/usr/bin/node

const myObject = {
  type: 'object',
  value: 12
};

console.log(myObject);

/**
 *  * Increment the value property of the object
 *   */
myObject.incr = function () {
  this.value++;
};

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
