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

const poll = mysql.createPool({
  connectionLimit: 10,
  waitForConnections: true, 
  queueLimit: 0,
  host: process.env.MYSQL_HOST || "localhost",
  user: process.env.MYSQL_USER || "root",
  password: process.env.MYSQL_PASSWORD || "mysql-pass",
  database: process.env.MYSQL_DB || "chat"
});

app.post('/save', (req, res) => {
  if (req.body.message) {
    saveMessage(req.body.message).then( id => {
      id ? res.status(200).send("Mensagem salva com sucesso! ID: " + id) : res.status(500).send("Erro ao salvar mensagem");
    });
  } else {
    res.status(204).send("Não salvamos mensagens vazias");
  }
});

async function saveMessage(msg) {
  const result = await poll.query('INSERT INTO messages SET message = ?', [msg]);
  if (result) {
    console.log("Mensagem Salva! - {" + msg + ": " + result[0].insertId + "}")
    return result[0].insertId;
  } 
  return null;
}
