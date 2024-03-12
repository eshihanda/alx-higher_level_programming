#!/usr/bin/node
const myArg = process.argv - 2;
if (myArg[0]) {
  console.log(myArg[0]);
} else {
  console.log('No argument');
}
