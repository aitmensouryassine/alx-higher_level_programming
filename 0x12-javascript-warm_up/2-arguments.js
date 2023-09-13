#!/usr/bin/node
const argCount = process.argv.length - 2;
console.log((argCount === 0) ? 'No argument' : (argCount === 1) ? 'Argument found' : 'Arguments found');
