var { conn, mysql } = require('../config/db')
var express = require('express')
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Datadog Demo :)' });
});

/* GET message listing. */
router.get('/search', (req, res) => {
  msg = req.query.msg;
  if (msg) {
    var sql = 'SELECT * FROM messages WHERE message = ' + mysql.escape(msg);
    execSQLQuery(sql, res);
  } else {
    var sql = 'SELECT * FROM messages ORDER BY id';  
    execSQLQuery(sql, res);
  }
});

router.post('/add', (req, res) => {
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

router.delete('/delete', (req, res) => {
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

function execSQLQuery(query, res) {
  conn.query(query, function(error, results){
    if (error) throw error;
    if (typeof results !== 'undefined' && results.length > 0) {
      res.status(200).json(results);
    } else {
      res.status(404).json({'message': 'Not Found'});
    }
  });
}

module.exports = router;
