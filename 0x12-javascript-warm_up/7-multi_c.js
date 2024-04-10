#!/usr/bin/node
const myArgs = process.argv.splice(2);
const num = Number(myArgs[0]);
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
	 for (i = 0; i < num; i++) {
		 console.log('C is fun');
	 }
}
