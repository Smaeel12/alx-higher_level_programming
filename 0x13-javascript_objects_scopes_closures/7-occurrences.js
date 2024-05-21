#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
	let counter = 0;
	for (let el of list) {
		if (el === searchElement) {
			counter++;
		}
	}
	return counter;
}
