const mongoose = require("mongoose");

// confirmed
// recovered
// deaths
// total
// total_visitor
// Time stamp

const schema = new mongoose.Schema({
  state: {
    type: String,
    required: true
  },
  confirmed: {
    type: Number,
    required: true
  },
  recovered: {
    type: Number,
    required: true
  },
  deaths: {
    type: Number,
    required: true
  },
  total: {
    type: Number,
    required: true
  },
  total_visitor: {
    type: Number,
  }
  
});

module.exports = mongoose.model("corona_data", schema);


// ,
//   time_stamp: {
//     type: Number,
//     required: true
//   }