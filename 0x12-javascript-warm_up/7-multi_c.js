#!/usr/bin/node
const repeatedString = parseInt(process.argv[2]);
let i = 0;
if (repeatedString) {
  for (i = 0; i < repeatedString; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
