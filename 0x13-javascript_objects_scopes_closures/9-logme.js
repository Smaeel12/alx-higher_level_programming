#!/usr/bin/node
exports.logMe = function (item) {
  this.nb = (this.nb || 0) + 1;
  console.log(this.nb - 1, ': ', item);
};
