// 101-sorted.js
#!/usr/bin/node

const { dict } = require('./101-data');

// Initialize an empty object for the sorted dictionary
const sortedDict = {};

// Iterate over each user id and occurrences in the original dict
for (const userId in dict) {
  const occurrences = dict[userId];

  // If the number of occurrences isn't a key in sortedDict, create it
  if (!sortedDict[occurrences]) {
    sortedDict[occurrences] = [];
  }

  // Push the current user id to the corresponding occurrences array
  sortedDict[occurrences].push(userId);
}

// Printing the sorted dictionary
console.log(sortedDict);
