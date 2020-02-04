#!/usr/bin/node
/* Script that prints two arguments passed to it */

const args = process.argv.slice(2);
if (args[0] === undefined) {
  console.log('No argument');
} else {
  console.log(args[0] + ' is ' + args[1]);
}
