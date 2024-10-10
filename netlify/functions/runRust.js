// netlify/functions/runRust.js
const { exec } = require('child_process');
const path = require('path'); 

exports.handler = async function(event, context) {
    const linuxBdatPath = path.join(__dirname, './linuxBDAT');
    console.log(linuxBdatPath);
    var fs = require('fs');
    var files = fs.readdirSync("/var/task");
    console.log(files);
    console.log('Current working directory:', __dirname);
  return new Promise((resolve, reject) => {
    exec(linuxBdatPath, (error, stdout, stderr) => {
      if (error) {
        console.error(`Error executing Rust binary: ${error}`);
        return reject({
          statusCode: 500,
          body: 'Server Error'
        });
      }

      resolve({
        statusCode: 200,
        body: stdout,
      });
    });
  });
};