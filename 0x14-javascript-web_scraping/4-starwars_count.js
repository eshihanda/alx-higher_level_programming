#!/usr/bin/node
// print number of movie where id 18 is present
const request = require('request');
const url = process.argv[2];
const character = 'https://swapi-api.alx-tools.com/api/people/18';
let number = 0;
request(url, (error, response, body) => {
  if (error) return console.error('Error:', error);
  for (const item of JSON.parse(body).results) {
    if (item.characters.includes(character)) {
      number += 1;
    }
  }
  console.log(number);
});
