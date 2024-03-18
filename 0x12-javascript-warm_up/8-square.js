#!/usr/bin/node
const myArgs = process.argv.slice(2);
const size = Number(myArgs[0]);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  let string = '';
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      string += 'X';
    }
    console.log(string);
    string = '';
  }
}
