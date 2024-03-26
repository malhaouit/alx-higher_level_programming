#!/usr/bin/node

const request = require('request');
const URL = process.argv[2];

request({ url: URL, json: true }, (err, response, body) => {
  if (err) {
    console.error('Error:', err);
    return;
  }

  if (response.statusCode === 200) {
    const completedTasksByUser = {};
    body.forEach(function (task) {
      if (task.completed) {
        if (!completedTasksByUser[task.userId]) {
          completedTasksByUser[task.userId] = 1;
        } else {
          completedTasksByUser[task.userId]++;
        }
      }
    });
    console.log(completedTasksByUser);
  }
});
