#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const obj = {};

request(url, (err, res, body) => {
  if (err) throw err;

  JSON.parse(body).forEach(todo => {
    const id = todo.userId;
    if (!obj[id]) obj[id] = 0;
    if (todo.completed) obj[id]++;
    if (obj[id] === 0) delete obj[id];
  });
  console.log(obj);
});
