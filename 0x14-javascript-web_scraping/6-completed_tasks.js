#!/usr/bin/node

const request = require('request');

// Get the API URL from command line argument
const apiUrl = process.argv[2];

// Function to count completed tasks per user
const countCompletedTasks = (data) => {
  const userTasks = {};

  // Iterate through each task
  data.forEach(task => {
    if (task.completed) {
      if (userTasks[task.userId]) {
        userTasks[task.userId]++;
      } else {
        userTasks[task.userId] = 1;
      }
    }
  });

  return userTasks;
};

// Fetch data from API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  try {
    // Parse JSON data
    const data = JSON.parse(body);
    // Get the count of completed tasks per user
    const completedTasks = countCompletedTasks(data);
    
    // Print only users with completed tasks
    console.log(completedTasks);
  } catch (e) {
    console.error(e);
  }
});
