#!/usr/bin/node
// prints title of a movie with a given id
const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;
request(url, (error, response, body) => {
  if (error) {
    return console.error('Error:', error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
