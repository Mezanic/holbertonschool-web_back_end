/**
 * Reads a file, counts the number of students in each field, and logs the results.
 *
 * @param {string} path - The path to the file containing student data.
 */

const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');
    const lines = data.split('\n').filter((line) => line.trim() !== '' && !line.startsWith('#'));

    const content = lines.slice(1);

    const students = {};

    content.forEach((line) => {
      const columns = line.split(',');
      const firstName = columns[0].trim();
      const field = columns[columns.length - 1].trim();

      if (field && firstName) {
        if (!students[field]) {
          students[field] = [];
        }
        students[field].push(firstName);
      }
    });

    let totalStudents = 0;
    for (const names of Object.values(students)) {
      totalStudents += names.length;
    }
    console.log(`Number of students: ${totalStudents}`);

    for (const [field, names] of Object.entries(students)) {
      console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
    }
  } catch (error) {
    console.error(error);
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
