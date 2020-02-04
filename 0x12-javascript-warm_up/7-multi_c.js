#!/usr/bin/node
/* Script that prints x times “C is fun" */

const lang = 'C is fun';
const argum = process.argv[2];
let i;

if (process.argv.length === 2) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < argum; i++) {
    console.log(lang);
  }
}
