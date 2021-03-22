#!/usr/bin/node
const _size = parseInt(process.argv[2]);
let i;
if (isNaN(_size)) {
  console.log('Missing size');
} else {
  for (i = 0; i < _size; i++) {
    console.log('X'.repeat(_size));
  }
}
