const express = require("express");
const app = express();
const NodeCache = require( "node-cache" );
const mongoose = require("mongoose");
const dotenv = require("dotenv");
const db_data = require("./Database/count_data");


const myCache = new NodeCache();
PORT=process.env.PORT || 3000;
dotenv.config();

app.use(express.json());
app.use(express.urlencoded({ extended: true }));


// confirmed
// recovered
// deaths
// total

//pass db  SAY6yEBz.iQf.C7
//mongodb+srv://AssamCoronaAdmin:<password>@cluster0-yxm6w.mongodb.net/test?retryWrites=true&w=majority 




//Db Connection
mongoose.connect(
  process.env.MONGO,
  { useUnifiedTopology: true, useNewUrlParser: true },
  () => {
    console.log("DB Connected");
  }
);




app.get("/api/getData/:state",async (req,res)=>{

	let state = req.params.state;
	total = myCache.get( state );
	if ( total == undefined ){
		//If cache miss return the data from db
		// let name = await db_data.findOne({}, {sort:{$natural:-1}});
    	res.json({status:400,error:"No data found"});
	}
	else {
		let current_data = myCache.get( state );
		
		res.json({status:200,state:state,current_data:current_data});
	}

});





app.post("/api/postData",async (req,res)=>{

	if(req.body){
		let { state,confirmed,recovered,deaths } = req.body;
		confirmed=parseInt(confirmed);
		recovered=parseInt(recovered);
		deaths=parseInt(deaths);
//res.json({data:confirmed});

		let reqDataRecord= { confirmed:confirmed, recovered:recovered, deaths:deaths , total:confirmed+recovered+deaths}

		//Storing in cache
		cache_store_success = myCache.set( state , reqDataRecord);
		// recovered_success = myCache.set( "recovered", recovered + current_cache_data.recovered);
		// deaths_success = myCache.set( "deaths", deaths + current_cache_data.deaths);


		//Checking if data is stored in cached
		if(!cache_store_success){
			res.json({status:400,error:"Some error occured try again"});
		}

		//Storing in DB
		let record = new db_data({
		  state:state,
	      confirmed: confirmed,
	      recovered: recovered,
	      deaths: deaths,
	      total:confirmed+recovered+deaths

	    });
	    try {
	      let saved_record = await record.save();
	      res.json({status:200})
	    } catch (err) {
	      res.json({status:400,error:err});
	    }
	}
	else {
		res.json({status:400,err:"No data posted"})
	}

});


















app.listen(PORT,()=>{
	console.log("Server is listening at Port:",PORT);
})