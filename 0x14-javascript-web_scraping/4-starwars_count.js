#!/usr/bin/node

const request = require('request');
const URL = process.argv[2];
const searchUrl = 'https://swapi-api.alx-tools.com/api/people/18/';

request({ url: URL, json: true }, (err, response, body) => {
  if (err) {
    console.error('Error:', err);
    return;
  }

  if (response.statusCode === 200) {
    let count = 0;
    body.results.forEach(film => {
      if (film.characters.includes(searchUrl)) {
        count++;
      }
    });
    console.log(count);
  }
});
