#!/usr/bin/node
let countLog = 0;
exports.logMe = function (item) { console.log(`${countLog++}: ${item}`); };
