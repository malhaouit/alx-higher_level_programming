#!/usr/bin/node

const request = require('request');
const filmId = process.argv[2];
const URL = `https://swapi-api.hbtn.io/api/films/${filmId}`;

request({ url: URL, json: true }, (err, response, body) => {
  if (err) {
    console.error('Error:', err);
    return;
  }

  body.characters.forEach(characterUrl => {
    request({ url: characterUrl, json: true }, (err, response, body) => {
      if (err) {
        console.error('Error:', err);
        return;
      }
      console.log(body.name);
    });
  });
});
