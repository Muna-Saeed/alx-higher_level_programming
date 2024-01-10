#!/usr/bin/node

const data = require('./101-data');

const occurrences = data.dict;

const sortedOccurrences = {};

Object.keys(occurrences).forEach(userId => {
  const occurrenceCount = occurrences[userId];

  if (!sortedOccurrences[occurrenceCount]) {
    sortedOccurrences[occurrenceCount] = [];
  }

  sortedOccurrences[occurrenceCount].push(userId.toString());
});

console.log(sortedOccurrences);
