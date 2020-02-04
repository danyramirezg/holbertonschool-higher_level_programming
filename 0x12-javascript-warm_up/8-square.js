#!/usr/bin/node
/* Script that prints a square */

const square = 'X';
const argum = process.argv[2];
let i;

if (isNaN(argum) || process.argv.length === 2) {
  console.log('Missing size');
} else {
  for (i = 0; i < argum; i++) {
    console.log(square.repeat(argum));
  }
}
