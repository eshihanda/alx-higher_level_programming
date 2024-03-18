#!/usr/bin/node
const myArgs = process.argv.slice(2);
function compare (a, b) {
  return a - b;
}
if (myArgs.length === 0) {
  console.log('0');
} else if (myArgs.length === 1) {
  console.log('0');
} else {
  console.log(myArgs.sort(compare)[myArgs.length - 2]);
}
