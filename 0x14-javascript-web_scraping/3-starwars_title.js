#!/usr/bin/node
// Prints the title of a Star Wars movie where the episode number matches a given integer.

const request = require('request');
const url = 'http://swapi.co/api/films/';

request(url + process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
