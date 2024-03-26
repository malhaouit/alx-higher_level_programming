#!/usr/bin/node

const request = require('request');
const URL = process.argv[2];

request({ url: URL, json: true }, (err, response, body) => {
  if (err) {
    console.error('Error:', err);
    return;
  }

  if (response.statusCode === 200) {
    let count = 0;
    body.results.forEach(film => {
      film.characters.forEach(characterUrl => {
        if (characterUrl.endsWith('18/')) {
          count++;
        }
      });
    });
    console.log(count);
  }
});
