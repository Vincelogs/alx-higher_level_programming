#!/usr/bin/node

const count = parseInt(process.argv[2]);
if (!count) {
  console.log('Missing number of occurrences');
} else if (count >= 0) {
  for (let i = 0; i < count; i++) {
    console.log('C is fun');
  }
}
