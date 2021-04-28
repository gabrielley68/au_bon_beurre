const express = require("express");
const path = require("path");
const mariadb = require('mariadb');
const db = require('./database.js');

/**const pool = mariadb.createPool({
	host: "127.0.0.1:3306",
	user: "root",
	password: "root"
});*/

const PORT = process.env.PORT || 3001;
const app = express();

app.use(express.static(path.resolve(__dirname, "../client/build")));

app.get("/records", async (req, res) => {
	//const records = await db.getRecords(pool);
	res.json({records: ["test", "test2"]});
});

app.get("/", (req, res) => {
	res.sendFile(path.resolve(__dirname, "../client/build", "index.html"));
})

app.listen(PORT, () => {
	console.log("Server listening");
});

