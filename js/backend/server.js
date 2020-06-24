const express = require("express");
const cors = require("cors");
const bodyParser = require("body-parser");
const mongoose = require("mongoose");
const sources = require("./models/sources");

mongoose.connect("mongodb://localhost:27017/printds", {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

const db = mongoose.connection;
db.once("open", () => {
  console.log("Database connected");
});

db.on("error", (err) => {
  console.error("connection error:", err);
});

require("dotenv").config();

const app = express();
const port = process.env.PORT || 5000;
app.listen(port, () => {
  console.log(`Server is running on port: ${port}`);
});

app.use(
  cors({
    origin: "http://localhost:3000",
  })
);
app.use(express.json());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.get("/api", (req, res) => {
  sources.aggregate(
    [{ $match: { status: true } }, { $sample: { size: 1 } }],
    function (err, result) {
      res.json(result);
      console.log(result);
    }
  );
});

app.get("/images/placeholder", (req, res) => {
  const path = require("path");
  const images = path.join(__dirname, "images");
  res.sendFile(path.join(images, "placeholder.jpg"));
  console.log(req.headers);
});
