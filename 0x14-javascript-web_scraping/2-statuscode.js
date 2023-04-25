#!/usr/bin/node
const request = require('request');
const base_url = process.argv[2];

request(base_url, (err, res, body) => {
  if (!err) console.log('code:', res.statusCode);
});
