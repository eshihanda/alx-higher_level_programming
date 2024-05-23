#!/usr/bin/node
// display the status code of a get request
const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
	  console.error('Error:', error);
  } else {
	  console.log('code:', response.statusCode);
  }
});
