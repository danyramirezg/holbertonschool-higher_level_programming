#!/usr/bin/node
// Script that writes a string to a file.

const fs = require('fs');

const data1 = process.argv[3];

fs.writeFile(process.argv[2], data1, 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  }
});
