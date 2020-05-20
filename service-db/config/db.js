var mysql = require("mysql2/promise");
var conn = mysql.createPool({
  connectionLimit: 10,
  waitForConnections: true, 
  queueLimit: 0,
  host: process.env.DB_HOST || "localhost",
  user: process.env.DB_USER || "datadog",
  password: process.env.DB_PASSWORD || "datadog",
  database: process.env.BD_NAME || "chat"
});

module.exports = {
  conn,
  mysql
}