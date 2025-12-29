const express = require('express');
const mysql = require('mysql2');
const app = express();

const db = mysql.createConnection({
  host: 'db',
  user: 'root',
  password: 'secret_password',
  database: 'user_db'
});

app.get('/', (req, res) => {
  db.query('SELECT COUNT(*) AS total FROM users', (err, results) => {
    if (err) res.send("DB not ready yet...");
    else res.send(`Total Users Registered: ${results[0].total}`);
  });
});

app.listen(3000);