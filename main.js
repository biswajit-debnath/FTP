let width = window.innerWidth;
		let height = window.innerHeight;
		let rad1 = Math.floor((0.65*width)/2); 
		var paper = Raphael("container", width,height);
			

		var dot = paper.circle(width/2, height/1, rad1*0.6).attr({ 
		
		stroke: "#999999", 
		"stroke-width":3,
		'stroke-opacity': 0,
		'fill-opacity':0  
		});
		var dot2 = paper.circle(width/2, height/1, rad1*0.45).attr({ 
		fill: "#FFF",
		stroke: "#999999", 
		"stroke-width": 3,
		'stroke-opacity': 0,
		'fill-opacity':0 
		});

		var dot3 = paper.circle(width/2, height/1, rad1*0.3).attr({ 
		fill: "#FFF",
		stroke: "#999999", 
		"stroke-width": 3,
		'stroke-opacity': 0,
		'fill-opacity':0 
		});

		var dot4 = paper.circle(width/2, height/1, rad1*0.1).attr({ 
		fill: "#FFF",
		stroke: "#999999", 
		"stroke-width": 3,
		'stroke-opacity': 0,
		'fill-opacity':0 
		});








	//Crime Circles

	let fill_var =0;
	let animate_sec=2500;
		// Smallest circle
		let lower_depth1=30;//30

		let delta_x_txt=27; //+ to rigth - to left
		let delta_y_txt=9;  //+to down -to up


		let crime_circle1_x = width/2+(rad1*0.15*Math.sin(0.698132));  
		let crime_circle1_y = lower_depth1+height/1.2+(rad1*0.15*Math.cos(0.698132)); 


		let circle_text_id1_y=crime_circle1_y+delta_y_txt;
		let circle_text1_y=crime_circle1_y+delta_y_txt+23;

		var crime_circle1 = paper.circle(crime_circle1_x,crime_circle1_y,16).attr({ 
			fill: "#DC67C9", 
			stroke: "#fff",
			"stroke-opacity":0, 
			'fill-opacity':fill_var 
		});

		
		var circle_text_id1 = paper.text( crime_circle1_x+delta_x_txt,circle_text_id1_y, "#4" ).attr({ 'font-size': 15,'font': "Arial, Helvetica, sans-serif",'font-weight': 'bold', fill:"#FFD6F8",'fill-opacity':fill_var });


		var circle_text1 = paper.text( crime_circle1_x+23+delta_x_txt,circle_text1_y, "Robery" ).attr({ 'font-size': 18,'font': "Arial, Helvetica, sans-serif",'font-weight': 'bold', fill:"#FFD6F8",'fill-opacity':fill_var});






		//2nd Smallest circle
		let lower_depth2=190; //160

		let delta_x_txt2=-55; //+ to rigth - to left
		let delta_y_txt2=-56;  //+to down -to up

		let crime_circle2_x = width/2+(rad1*0.4*Math.sin(2.26893));
		let crime_circle2_y = lower_depth2+height/1.2+(rad1*0.4*Math.cos(2.26893));


		let circle_text_id2_y=crime_circle2_y+delta_y_txt2;
		let circle_text2_y=crime_circle2_y+delta_y_txt2+23;

		var crime_circle2 = paper.circle(crime_circle2_x,crime_circle2_y,20).attr({ 
			fill: "#DC9A67", 
			stroke: "#fff",
			'fill-opacity':fill_var,
			"stroke-opacity":0
		});

		
		var circle_text_id2 = paper.text( crime_circle2_x+delta_x_txt2,circle_text_id2_y, "#3" ).attr({ 'font-size': 15,'font': "Arial, Helvetica, sans-serif",'font-weight': 'bold', fill:"#FFE8D6",'fill-opacity':fill_var});


		var circle_text2 = paper.text( crime_circle2_x+39+delta_x_txt2,circle_text2_y, "Kidnapping" ).attr({ 'font-size': 18,'font': "Arial, Helvetica, sans-serif",'font-weight': 'bold', fill:"#FFE8D6",'fill-opacity':fill_var});




		//3nd Smallest circle
		let lower_depth3=70; //70
		
		let delta_x_txt3=39; //+ to rigth - to left
		let delta_y_txt3=-54;  //+to down -to up
		
		let crime_circle3_x = width/2-(rad1*0.7*Math.sin(1.5708));
		let crime_circle3_y = lower_depth3+height/1.2+(rad1*0.7*Math.cos(1.5708));


		let circle_text_id3_y=crime_circle3_y+delta_y_txt3;
		let circle_text3_y=crime_circle3_y+delta_y_txt3+23;


		var crime_circle3 = paper.circle(crime_circle3_x,crime_circle3_y,30).attr({ 
			fill: "#DC6767", 
			stroke: "#fff",
			'fill-opacity':fill_var,
			"stroke-opacity":0
		});

		
		var circle_text_id3 = paper.text( crime_circle3_x+delta_x_txt3,circle_text_id3_y, "#2" ).attr({ 'font-size': 15,'font': "Arial, Helvetica, sans-serif",'font-weight': 'bold', fill:"#FBCACA",'fill-opacity':fill_var});


		var circle_text3 = paper.text( crime_circle3_x+23+delta_x_txt3,circle_text3_y, "Murder" ).attr({ 'font-size': 18,'font': "Arial, Helvetica, sans-serif",'font-weight': 'bold', fill:"#FBCACA",'fill-opacity':fill_var});




		//Big circle
		 lower_depth4=420;

		let delta_x_txt4=54; //+ to rigth - to left
		let delta_y_txt4=-25;  //+to down -to up


		let crime_circle4_x = width/2+(rad1*Math.sin(2.53073));
		let crime_circle4_y = lower_depth4+height/1.2+(rad1*Math.cos(2.53073));



		let circle_text_id4_y=crime_circle4_y+delta_y_txt4;
		let circle_text4_y=crime_circle4_y+delta_y_txt4+23;


		var crime_circle4 = paper.circle(crime_circle4_x,crime_circle4_y,40).attr({ 
			fill: "#67DCAD", 
			stroke: "#fff",
			'fill-opacity':fill_var,
			"stroke-opacity":0
		});

		
		var circle_text_id4 = paper.text( crime_circle4_x+delta_x_txt4,circle_text_id4_y, "#1" ).attr({ 'font-size': 15,'font': "Arial, Helvetica, sans-serif",'font-weight': 'bold', fill:"#D0FBEA",'fill-opacity':fill_var});


		var circle_text4 = paper.text( crime_circle4_x+14+delta_x_txt4,circle_text4_y, "Rape" ).attr({ 'font-size': 18,'font': "Arial, Helvetica, sans-serif",'font-weight': 'bold', fill:"#D0FBEA",'fill-opacity':fill_var});


		function animateball1() {
			dot.animate({'r': rad1, 'stroke-opacity' :0.4, 'cy':height/1.2, 'fill': '#FFF' }, animate_sec, "backOut" );
			dot2.animate({'r': rad1*0.7, 'stroke-opacity' :0.4,'cy':height/1.2, 'fill': '#FFF' }, animate_sec, "backOut" );
			dot3.animate({'r': rad1*0.4,'stroke-opacity' :0.4, 'cy':height/1.2, 'fill': '#FFF' }, animate_sec, "backOut" );
			dot4.animate({'r': rad1*0.15,'stroke-opacity' :0.4, 'cy':height/1.2, 'fill': '#FFF' }, animate_sec, "backOut" );


			//1st Smallest 
			crime_circle1.animate({'cy':crime_circle1_y-lower_depth1,'fill-opacity':1},animate_sec,"backOut")
			circle_text_id1.animate({'y':circle_text_id1_y-lower_depth1,'fill-opacity':1},animate_sec,"backOut")
			circle_text1.animate({'y':circle_text1_y-lower_depth1,'fill-opacity':1},animate_sec,"backOut")





			//2nd Smallest 
			crime_circle2.animate({'cy':crime_circle2_y-lower_depth2,'fill-opacity':1},animate_sec,"backOut")
			circle_text_id2.animate({'y':circle_text_id2_y-lower_depth2,'fill-opacity':1},animate_sec,"backOut")
			circle_text2.animate({'y':circle_text2_y-lower_depth2,'fill-opacity':1},animate_sec,"backOut")




			//3rd Smallest 
			crime_circle3.animate({'cy':crime_circle3_y-lower_depth3,'fill-opacity':1},animate_sec,"backOut")
			circle_text_id3.animate({'y':circle_text_id3_y-lower_depth3,'fill-opacity':1},animate_sec,"backOut")
			circle_text3.animate({'y':circle_text3_y-lower_depth3,'fill-opacity':1},animate_sec,"backOut")





			//4th Smallest 
			crime_circle4.animate({'cy':crime_circle4_y-lower_depth4,'fill-opacity':1},animate_sec,"backOut")
			circle_text_id4.animate({'y':circle_text_id4_y-lower_depth4,'fill-opacity':1},animate_sec,"backOut")
			circle_text4.animate({'y':circle_text4_y-lower_depth4,'fill-opacity':1},animate_sec,"backOut")
		}   



		function animateball2() {
			dot.animate({'cy':height/0.75}, animate_sec, "backOut" );
			dot2.animate({'cy':height/0.75}, animate_sec, "backOut" );
			dot3.animate({'cy':height/0.75}, animate_sec, "backOut" );
			dot4.animate({'cy':height/0.75}, animate_sec, "backOut" );


			//1st Smallest 
			crime_circle1.animate({'cx':width/1.2,'fill-opacity':0},animate_sec,"backOut")
			circle_text_id1.animate({'x':width/1.2,'fill-opacity':0},animate_sec,"backOut")
			circle_text1.animate({'x':width/1.2,'fill-opacity':0},animate_sec,"backOut")





			//2nd Smallest 
			crime_circle2.animate({'cx':width/1.15,'fill-opacity':0},animate_sec,"backOut")
			circle_text_id2.animate({'x':width/1.15,'fill-opacity':0},animate_sec,"backOut")
			circle_text2.animate({'x':width/1.15,'fill-opacity':0},animate_sec,"backOut")




			//3rd Smallest 
			crime_circle3.animate({'cx':width/1.5,'fill-opacity':0},animate_sec,"backOut")
			circle_text_id3.animate({'x':width/1.5,'fill-opacity':0},animate_sec,"backOut")
			circle_text3.animate({'x':width/1.5,'fill-opacity':0},animate_sec,"backOut")





			//4th Smallest 
			crime_circle4.animate({'cx':width,'fill-opacity':0},animate_sec,"backOut")
			circle_text_id4.animate({'x':width,'fill-opacity':0},animate_sec,"backOut")
			circle_text4.animate({'x':width,'fill-opacity':0},animate_sec,"backOut")
		}  
		setTimeout(animateball1,1000);
		setTimeout(animateball2, 4000);








//Title animation


setTimeout(()=>{

	$(".title_author_txt").addClass("title_author_txt_slided");
	$(".title_txt").addClass("title_txt_slided");





	$(".svg_ln").addClass("line_animate");


	$(".title_line").addClass("title_line_animate");
},1000);


//Arrow animation
setTimeout(()=>{
	$(".arrow_container").addClass("arrow_container_slided");
},4600);












//Menu bar animation

// let line = document.getElementById("Line_17-2");
// line.x2.baseVal.value = 25;

function menuClickHandler(){
	//Toggle in b/w X and stright line
	let menu_element = document.getElementById("menu");
	menu_element.classList.toggle("nav_hover");
	$(".cls-2").addClass("cls-2_cross");
	$(".cls-3").addClass("cls-3_cross");
	$(".cls-4").addClass("cls-4_cross");




	//Create the lightbox effect
	$(".light_box").addClass("light_box_overlay");
	$(".overlay_circle").show();

	$(".main").addClass("main_overlay");

	//body overlay op change to reduce the op of the characters
	$(".overlay").addClass("overlay_opacity");


	$(".overlay_menu_container").addClass("overlay_menu_container_show");


	setTimeout(()=>{
		$(".overlay_circle").addClass("overlay_circle_show");
		setTimeout(()=>{
			$(".about_link").addClass("about_link_show");
			$(".system_link").addClass("system_link_show");
		},800);
		
	},200);

} 


function OverlaymenuClickHandler(){
	$(".cls-2").removeClass("cls-2_cross");
	$(".cls-3").removeClass("cls-3_cross");
	$(".cls-4").removeClass("cls-4_cross");




	//Create the lightbox effect
	$(".light_box").removeClass("light_box_overlay");
	$(".overlay_circle").hide();

	$(".main").removeClass("main_overlay");

	//body overlay op change to reduce the op of the characters
	$(".overlay").removeClass("overlay_opacity");


	$(".overlay_menu_container").removeClass("overlay_menu_container_show");



	//Remove the circle and link animated class to restart the animation
	$(".overlay_circle").removeClass("overlay_circle_show");
	$(".about_link").removeClass("about_link_show");
	$(".system_link").removeClass("system_link_show");
}













//Sliding Animation

 //home and assam up
 function upSlider(){
 	$(".assam").addClass("assam_slided-up");
  	$(".home").addClass("home_slided-up");
  	setTimeout(()=>{
  		$(".assam_title").addClass("assam_title_slided");
  		$(".assam_count_container").addClass("assam_count_container_slided");
  	},2000);

 }

 function downSlider(){
 	$(".assam").removeClass("assam_slided-up");
  	$(".home").removeClass("home_slided-up");
 }



 //About Page
 function AboutSlider(){
 	$(".about").addClass("about_slided");
 	$(".home").addClass("home_slided-right");
 }

 //System Page
 function systemSlider() {
 	$(".system").addClass("system_slided");
 	$(".home").addClass("home_slided-right");	
 }


 //Landing Page About and system
 function AboutPageBackSlide(){
 	$(".about").removeClass("about_slided");
 	$(".home").removeClass("home_slided-right");		
 }
 function SystemPageBackSlide(){
 	$(".system").removeClass("system_slided");
 	$(".home").removeClass("home_slided-right");		
 }












 //Analyz Page
 function analyzSlider(){
 	$(".analyz").addClass("analyz_slided-left");
 	$(".home").addClass("home_slided-left");
 }