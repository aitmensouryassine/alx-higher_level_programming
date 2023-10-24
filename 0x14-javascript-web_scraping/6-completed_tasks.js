#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

const data = {};
request(url, (err, res, body) => {
  if (err) return;

  const todos = JSON.parse(body);
  todos.forEach(todo => {
    if (!(todo.userId in data) && todo.completed) {
      data[todo.userId] = 0;
    }
    if (todo.completed) {
      data[todo.userId] += 1;
    }
  });
  console.log(data);
});
