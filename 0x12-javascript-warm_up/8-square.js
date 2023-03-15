#!/usr/bin/node

const arg = process.argv[2];
if (!parseInt(arg)) {
  console.log('Missing size');
} else {
  const count = Math.round(arg);
  for (let i = 0; i < count; i++) {
    let i = '';
    for (let j = 0; j < count; j++) i += 'X';
    console.log(i);
  }
}
