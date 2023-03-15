#!/usr/bin/node

const args = process.argv.slice(2);
const len = args.length;

if (len < 2) {
  console.log(0);
} else {
  const nums = args.map(Number);
  const max1 = Math.max(...nums);
  nums.splice(nums.indexOf(max1), 1);
  const max2 = Math.max(...nums);
  console.log(max2);
}
