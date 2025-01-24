// This module prompts the user for their name and logs it to the console.
const readline = require('node:readline');
const { stdin: input, stdout: output } = require('node:process');

const rl = readline.createInterface({ input, output });

rl.question('Welcome to Holberton School, what is your name?', (answer) => {
  console.log(`Your name is: ${answer}`);

  rl.close();
  if (!process.stdin.isTTY) {
    console.log('This important software is now closing');
  }
});
