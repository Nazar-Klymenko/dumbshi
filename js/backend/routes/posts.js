const express = require("express");
const router = express.Router();
const app = express();

app.post("/", (req, res) => {
  const id = req.body.id;
  res.json(id);
});

module.exports = router;
