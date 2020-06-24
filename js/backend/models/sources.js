const mongoose = require("mongoose");
const Schema = mongoose.Schema;

// const sourcesSchema = new Schema(
//   { img_id: String, checked: Boolean, source: String, status: Boolean },
//   { collection: "question" }
// );

// const sourcesSchema = new Schema({
//   img_id: String,
//   checked: Boolean,
//   source: String,
//   status: Boolean,
// });
mongoose.model(
  "sources",
  new Schema({
    img_id: String,
    checked: Boolean,
    source: String,
    status: Boolean,
  }),
  "ids"
);
module.exports = mongoose.model("sources");
