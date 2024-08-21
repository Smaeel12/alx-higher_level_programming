#!/usr/bin/node
const request = require('request');

request.get(process.argv[2], function (err, response, body) {
  if (err) throw new Error(err);
  const tasks = JSON.parse(body);
  console.log(tasks.reduce(function (total, item) {
    if (item.completed) { total[item.userId] = (total[item.userId] || 0) + 1; }
    return total;
  }, {}));
});

// request.get(process.argv[2], function (err, response, body) {
//     tasks = JSON.parse(body)
//     let users = {}
//     for (task of tasks)
//         if (task.completed === true) {
//             users[task.userId] = (users[task.userId] + 1) || 1
//         }
//     console.log(users)
// })
