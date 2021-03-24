#!/usr/bin/node
const _argument = process.argv;
if (_argument.length <= 3) {
  console.log(0);
} else {
  /* slice returns a shallow copy of a portion of an array
  and indicates (-2) extracts the last two elements in the sequence */
  /* sort accepts a comparative fuction which in this case
  organizes values in ascendent order */
  console.log(_argument.slice(2).sort((a, b) => a - b).reverse()[1]);
}
