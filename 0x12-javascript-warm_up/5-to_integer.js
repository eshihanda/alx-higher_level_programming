#!/usr/bin/node
const myArg = process.argv.slice(2);
const num = Number(myArg[0]);
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + num);
}
