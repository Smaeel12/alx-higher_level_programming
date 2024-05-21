#!/usr/bin/node

exports.esrever = function (list) {
	let new_list = [];
	for (let i = list.length - 1; i >= 0; i--) {
		new_list.push(list[i])
	}
	return new_list;
}
