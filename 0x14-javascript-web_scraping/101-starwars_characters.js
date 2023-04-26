#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, (err, res, body) => {
  if (err) throw err;
  const characters = JSON.parse(body).characters;
  printChars(characters, 0);
});

function printChars (characters, idx) {
  request(characters[idx], (err, res, body) => {
    if (err) throw err;
    console.log(JSON.parse(body).name);
    if (idx + 1 < characters.length) printChars(characters, idx + 1);
  });
}
