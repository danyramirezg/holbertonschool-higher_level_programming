#!/usr/bin/node
// Prints the number of movies where the character “Wedge Antilles” is present.

const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const resul = JSON.parse(body).results;
    let movies = 0;
    for (let i = 0; i < resul.length; i++) {
      const c = resul[i].characters;
      for (let j = 0; j < c.length; j++) {
        if (c[j].includes('18')) {
          movies++;
        }
      }
    }
    console.log(movies);
  }
});
