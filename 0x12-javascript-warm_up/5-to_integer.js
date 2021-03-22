#!/usr/bin/node
const _parsed = parseInt(process.argv[2]);
if (isNaN(_parsed)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + _parsed);
}
