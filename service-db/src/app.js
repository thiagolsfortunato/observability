#!/usr/bin/env node
const mysql = require("mysql2/promise");
const express = require("express");
const bodyParser = require('body-parser');
const port = process.env.PORT || 3000;
const app = express();

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.listen(port);

console.log(`Aplicação teste executando em http://localhost:${port}/`);

const conn = mysql.createPool({
  connectionLimit: 10,
  waitForConnections: true, 
  queueLimit: 0,
  host: process.env.DB_HOST || "localhost",
  user: process.env.DB_USER || "datadog",
  password: process.env.DB_PASSWORD || "datadog",
  database: process.env.BD_NAME || "chat"
});

app.get('/search', (req, res) => {
  msg = req.query.msg; 
  if (msg) {
    var sql = 'SELECT * FROM messages WHERE message = ' + mysql.escape(msg);
    execSQLQuery(sql, res);
  } else {
    var sql = 'SELECT * FROM messages ORDER BY id';  
    execSQLQuery(sql, res);
  }
});

app.post('/add', (req, res) => {
  msg = req.query.msg;
  if (msg) {
    var select_sql = 'SELECT * FROM messages WHERE message = ' + mysql.escape(msg);
    conn.query(select_sql, function(error, results) {
      if (error) throw error;
      if (results.length == 0) {
        var sql = 'INSERT INTO messages SET message = ' + mysql.escape(msg);
        conn.query(sql, function(error, results) {
          if (error) throw error;
          if (results.insertId) res.status(200).json({'id': results.insertId});
          else res.status(400).json({'message': 'Error to execute'})
        });
      } else {
        res.status(409).json({'message': 'Message already exists!'})
      }
    });
  } else {
    res.status(204).json({'message': 'Missing attribute msg'});
  }
});

app.delete('/delete', (req, res) => {
  msg = req.query.msg;
  if (msg) {
    sql = 'DELETE FROM messages WHERE message = ' + mysql.escape(msg);
    conn.query(sql, function(error, results) {
      if (error) throw error;
      if (typeof results !== 'undefined' && results.affectedRows > 0) {
        res.status(200).json({'rows affected': results.affectedRows});
      } else {
        res.status(400).json({'message': 'Error to delete rows'})
      }
    });
  } else {
    res.status(204).json({'message': 'Missing attribute msg'});
  }
});

function execSQLQuery(query, res){
  conn.query(query, function(error, results){
    if (error) throw error;
    if (typeof results !== 'undefined' && results.length > 0) {
      res.status(200).json(results);
    } else {
      res.status(404).json({'message': 'Not Found'});
    }
  });
}
