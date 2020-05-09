const cluster_index_name = ['V_High', 'High','Low','V_Low'];


// const selection= $('.radio:checked').val();
// if(selection === "Entire") {
// 	$('#crime').disabled = true;
// }

$(document).ready(function(){
	let State_selected=null;
	let selection= null;


	//Year wise analysis
	$('#list').on('click', function(ev){
		$('.bar_plot').show();


		total_data=[];
		top_data=[];
		second_top_data=[];
		

		if(selection != "Entire_NE"){

			target_district = ev.target.parentNode.className;
			// console.log('dist',target_district)
			$.ajax({
				data : {
					district : target_district,
					state : State_selected
				},
				type : 'POST',
				url : '/backend/Entire/year'
			})
			.done(function(data){
				top_crime = data["top_crime_list"]["top"];
				second_top_crime = data["top_crime_list"]["Second_top"]; 
				total_obj= data["total"];
				// console.log(total_obj);
				top_obj=data["top_crime"];
				second_obj= data["second_top_crime"];



				for (let obj in total_obj){
					//Getting the total crime data
					temp_obj={ y:total_obj[obj], label: obj.toString(10)};
					total_data.push(temp_obj);
				}
				
				for (let obj in top_obj){
					//Getting the top crime data
					temp_obj = { y:top_obj[obj], label: obj.toString(10)};
					top_data.push(temp_obj);
				}

				for (let obj in second_obj){
					//Getting the top crime data
					temp_obj = { y:second_obj[obj], label: obj.toString(10)};
					second_top_data.push(temp_obj);
				}
				console.log(total_data,top_data,second_top_data);

				district_name=target_district.toLowerCase();
				bar_plot(total_data,top_data,second_top_data,top_crime,second_top_crime,district_name,State_selected);

			});
		}

		else {

			
			// console.log('dist',target_district)
			State_selected = ev.target.parentNode.className;
			State_selected = State_selected.toLowerCase();
			First_letter= State_selected.charAt(0).toUpperCase();
			substring = State_selected.substring(1);
			State_selected = First_letter+substring;
			$.ajax({
				data : {
					state : State_selected
				},
				type : 'POST',
				url : '/backend/Entire_NE/year'
			})
			.done(function(data){
				top_crime = data["top_crime_list"]["top"];
				second_top_crime = data["top_crime_list"]["Second_top"]; 
				total_obj= data["total"];
				// console.log(total_obj);
				top_obj=data["top_crime"];
				second_obj= data["second_top_crime"];



				for (let obj in total_obj){
					//Getting the total crime data
					temp_obj={ y:total_obj[obj], label: obj.toString(10)};
					total_data.push(temp_obj);
				}
				
				for (let obj in top_obj){
					//Getting the top crime data
					temp_obj = { y:top_obj[obj], label: obj.toString(10)};
					top_data.push(temp_obj);
				}

				for (let obj in second_obj){
					//Getting the top crime data
					temp_obj = { y:second_obj[obj], label: obj.toString(10)};
					second_top_data.push(temp_obj);
				}
				console.log(total_data,top_data,second_top_data);

				district_name= State_selected;
				bar_plot(total_data,top_data,second_top_data,top_crime,second_top_crime,district_name,State_selected);

			});
		}
	});

	// total_obj=[
	//       { y: 243, label: "2001" },
 //          { y: 236, label:  "2002"},
 //          { y: 243, label:  "2003"},
 //          { y: 273, label:  "2004"},
 //          { y: 269, label:  "2005"},
 //          { y: 196, label:  "2006"},
 //          { y: 1118, label:  "2007"},
 //          { y: 1118, label:  "2008"},
 //          { y: 1118, label:  "2009"},
 //          { y: 1118, label:  "2010"},
 //          { y: 1118, label:  "2011"},
 //          { y: 1118, label:  "2012"}
 //        ];

    
	
	// $( ".alert" ).delay( 800 ).fadeIn( 400 );
	// $('.alert').delay(9000).show();

	//Ajax request for entire crime category for a selected state
	$('form').on('submit', function(ev){
		State_selected=$('#state').val();
		empty_list();
		$('.bar_plot').hide();


		selection= $('.radio:checked').val();
		
		if(selection === "Entire") {
			$.ajax({
						data : {
							name : $('#name').val(),
							state : $('#state').val()
							
						},
						type : 'POST',
						url : '/backend/Entire'
					})
					.done(function(data){
						
						if(data.err) {
		
							$( "#failed" ).text(data.err).delay( 500 ).fadeIn( 400 );
							$( "#sucess" ).hide();
						}
						else {
		
							$( '#list' ).show();
							for(const district in data){
								result=data[district];
								create_li(result,district);
							}
							console.log(data)
							$( "#sucess" ).text('Sucess').delay( 500 ).fadeIn( 400 ).delay(4000).fadeOut(400);
							$( "#failed" ).hide();
						}
					});
		}
		else if( selection === "Entire_NE") {
			//Ajax request for entire crime category for Entire North East
			$.ajax({
						data : {
							name : $('#name').val()
							
						},
						type : 'POST',
						url : '/backend/Entire_NE'
					})
					.done(function(data){
						
						if(data.err) {
		
							$( "#failed" ).text(data.err).delay( 500 ).fadeIn( 400 );
							$( "#sucess" ).hide();
						}
						else {
		
							$( '#list' ).show();
							for(const state in data){
								result=data[state];
								create_li(result,state);
							}
							console.log(data)
							$( "#sucess" ).text('Sucess').delay( 500 ).fadeIn( 400 ).delay(4000).fadeOut(400);
							$( "#failed" ).hide();
						}
					});

		}
		else {
			//Ajax request for a selected crime category for a selected state
			$.ajax({
						data : {
							name : $('#name').val(),
							crime: $('#crime').val(),
							state : $('#state').val()
							
						},
						type : 'POST',
						url : '/backend/Individual'
					})
					.done(function(data){
						
						if(data.err) {
		
							$( "#failed" ).text(data.err).delay( 500 ).fadeIn( 400 );
							$( "#sucess" ).hide();
						}
						else {
		
							$( '#list' ).show();
							for(const district in data){
								result=data[district];
								create_li(result,district);
							}
							console.log(data)
							$( "#sucess" ).text('Sucess').delay( 500 ).fadeIn( 400 ).delay(4000).fadeOut(400);
							$( "#failed" ).hide();
						}
					});
		}
		ev.preventDefault();

	})
});

function create_li(text,district){
	const id = `#${text}`;
	const li = document.createElement('li');
	li.className=`${district}`;
	const btn = document.createElement('button');
	btn.className= "btn btn-success btn-sm ml-3 mb-3";
	btn.innerText = "Analysis";
	li.innerText = `${district}`;
	$(id).append(li);
	const dis_list_cls=`.${district}`;
	$(dis_list_cls).append(btn);	
}

function empty_list(){
	cluster_index_name.forEach(cluster=>{
		const li_id = `#${cluster}`;
		$(li_id).empty();
	});
}




function bar_plot(total_obj,top_obj,second_obj,top_crime,second_top_crime,district,state){


    var chart = new CanvasJS.Chart("chartContainer", {
      animationEnabled: true,
      title:{
        text: `Year-Wise analysis of crime in ${district} district of ${state}`
      },
      axisY: {
        title: "Crime Analysis"
      },
      legend: {
        cursor:"pointer",
        itemclick : toggleDataSeries
      },
      toolTip: {
        shared: true,
        content: toolTipFormatter
      },
      data: [{
        type: "bar",
        showInLegend: true,
        name: "Total Crime ",
        color: "gold",
        dataPoints: total_obj
      },
      {
        type: "bar",
        showInLegend: true,
        name: top_crime,
        color: "silver",
        dataPoints: top_obj
      },
      {
        type: "bar",
        showInLegend: true,
        name: second_top_crime,
        color: "#A57164",
        dataPoints: second_obj
      }]
    });
    chart.render();

    function toolTipFormatter(e) {
      var str = "";
      var total = 0 ;
      var str3;
      var str2 ;
      for (var i = 0; i < e.entries.length; i++){
        var str1 = "<span style= \"color:"+e.entries[i].dataSeries.color + "\">" + e.entries[i].dataSeries.name + "</span>: <strong>"+  e.entries[i].dataPoint.y + "</strong> <br/>" ;
        total = e.entries[i].dataPoint.y + total;
        str = str.concat(str1);
      }
      str2 = "<strong>" + e.entries[0].dataPoint.label + "</strong> <br/>";
      str3 = "<span style = \"color:Tomato\">Total: </span><strong>" + total + "</strong><br/>";
      return (str2.concat(str)).concat(str3);
    }

    function toggleDataSeries(e) {
      if (typeof (e.dataSeries.visible) === "undefined" || e.dataSeries.visible) {
        e.dataSeries.visible = false;
      }
      else {
        e.dataSeries.visible = true;
      }
      chart.render();
    }

  
}