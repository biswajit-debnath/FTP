const express = require("express");
const router = express.Router();



router.get("/:state",async (req,res)=>{

	let state = req.params.state;
	// total = myCache.get( state );
	// if ( total == undefined ){
	// 	//If cache miss return the data from db
	// 	// let name = await db_data.findOne({}, {sort:{$natural:-1}});
 //    	res.json({status:400,error:"No data found"});
	// }
	// else {
	// 	let current_data = myCache.get( state );
		
	// 	res.json({status:200,state:state,current_data:current_data});
	// }
	res.json({data:state})

});





module.exports = router;