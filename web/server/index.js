const express = require("express");
const path = require("path");

const PORT = process.env.PORT || 3001;
const app = express();

app.use(express.static(path.resolve(__dirname, "../client/build")));

app.get("/records", (req, res) => {
	res.json({records: []});
});

app.get("/", (req, res) => {
	res.sendFile(path.resolve(__dirname, "../client/build", "index.html"));
})

app.listen(PORT, () => {
	console.log("Server listening");
});

