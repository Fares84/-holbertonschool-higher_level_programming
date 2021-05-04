#!/usr/bin/node
const fs = require('fs');
const fileName = process.argv[2];
const dataFile = process.argv[3];

fs.writefile(fileName, dataFile, 'utf-8', (error) => {
  if (error) {
    console.log(error);
  }
});
