// JavaScript Document




var traits_full = 
	['capable', 'comfortable', 'communicative', 'confident', 'energetic', 
	 'friendly', 'fun and entertaining', 'giving', 'happy', 'hardworking',
	 'independent', 'intelligent', 'interested', 'lovable', 'mature', 'needed', 
	 'optimistic', 'organized', 'outgoing', 'successful','disagreeing', 'disorganized', 'hopeless', 'immature', 'incompetent', 'indecisive', 'inferior', 'insecure', 'irresponsible', 'irritable', 
	 'isolated', 'lazy', 'like a failure', 'sad and blue', 'self-centered', 
	 'tense', 'uncomfortable', 'unloved', 'weary', 'worthless']



$(document).ready(function() {

	var traits_arr = [] // current array containing traits

	var self_count = 1 // This defines the self-aspect number

	var dic_self={} // This is where someone's self-aspects are stored. Make this a global variable. 
	var dic_trait={} // This is the dictionary where traits are stored. 

	var edit = false; // This tells us whether something is in the state of being edited or not- if it's being edited then we want to replace it. It's important to change editing back to 
	// false in the code, once the editing is done. 

	once = false;
	once1 = false;
	once2 = false; 

	$("#section-header-0").show();

	$("#instructions").show();


	// add years to age question
	for(i=2000;i>1900;i--)
	{
		$("#age").append('<option value="'+i+'">'+i+'</option>');
	}


	//This part just displays the inital introduction


	



	//This function is to proceed from the first intro page. 

	$("#fin_intro").click(function() {

		$("#section-header-0").hide();
		$("#instructions").hide(500);
		$("#demographics_h").show();
		$("#demo-wrapper").show(500);




	});



	

	$("#fin_demo").click(function() {
		

		checkDemographics();
		

		
		
	});


	function checkDemographics()
{
    gender = $("input[name=gender]:checked").val();
    age = $("#age option:selected").val();
    loc = $("#sel_country option:selected").val();
    races = [];
    $("input[name=race]:checked").each(function() { races.push($(this).val()); });
    income = $("#income option:selected").val();
    education = $("#edu option:selected").val();

    // alert(income+"\n"+parseFloat(income)+"\n");
    // $.get('getLocation.php', 
    //         { 'q': loc},
    //         function(data) {
    //             alert(data);
    //         });

    // Do validation of input
    var error = false;
    var errmsg = "";
	//$("li").addClass("black");

    if(gender==null)
	{
	    error=true;
	    //errmsg += "<div class='error'>Please choose an option for gender</div>";
		//$("#genderq").addClass("error");
		$("#genderq").css('color','red');
		
	} 
	
	   
    if(age=="unselected")
	{
	    error=true;
	    //errmsg += "<div class='error'>Please state the year you were born</div>";
		$("#ageq").addClass("error");
	}
	
		
	
    if(loc == "unselected")
	{
	    error=true;
	    //errmsg += "<div class='error'>Please indicate your current location</div>";
		$("#locationq").addClass("error");
	}
	
    if(races.length==0)
	{
	    error=true;
	    errmsg += "<div class='error'>Please indicate your ethnicity</div>";
		$("#ethnicityq").addClass("error");
	}
	
    if(income=="unselected" || $.trim(income) != income.replace(/[^0-9$.,]/g,'') || !IsNumeric(income.replace(/[^0-9.]/g,'')))
	{
	    error=true;
	    //errmsg += "<div class='error'>Please enter a valid number for income</div>";
		$("#incomeq").addClass("error");
	}
	
    if(education=="unselected")
	{
	    error=true;
	    errmsg += "<div class='error'>Please indicate your highest level of education</div>";
		$("#educationq").addClass("error")
	}
	
    // Output error message if input not valid
    if(error==false || once == true)
	{
	    twitid = $("#twitid").html();
	    $.post("core/DataWrangler.php", {"page":"demog", "twitid":twitid, "data":{"gender":gender,"age":age,"loc":loc,"races":races,"income":income,"edu":education} });
	    $("#demographics_h").hide();
		$("#demo-wrapper").hide(500);

	    //$("#demographics_h").hide();
	    //$("#demo-wrapper").hide(500);
		once = false;

		
		//initiate the political affiliation bit

		$("#politics_h").show();
		$("#GetPol-wrapper").show(500);



	}
    else
	{
	    $('#error-1').html('Oops. We noticed you left one or more items blank (shown in red above). Your responses are most useful to us when you answer every question, so we would appreciate it if you fill those in. But if you choose not to answer those specific items, you can press "Submit" to move on.');
		once = true;
	}
	
}


$("#fin_politics").click(function() {
		checkPolitics();

	});



function checkPolitics()
{
	party =$("#affiliation option:selected").val();

	var error = false;
	var errmsg= "";
	var wrapper = "#displayQ-wrapper_" + "party";
	iden = "party";
	
	if(once == true && party=="unselected")

	{   // This the the case where someone has been warned they didn't input the politics field- and still chooses
//to move on- instead of directing them to the subsequent politics questions, it takes them to the free-response identity portion. 
		
		$("#politics_h").hide();
		$("#GetPol-wrapper").hide(500); 
		once=false;


		
		
		$("#free_h").show();
	    $("#FreeForm-wrapper").show(500);
	    // reset this variable for the next section
	




		

		
}


	else

	{
	
	

	if(party == "unselected")
	{ 
	    once = true; 
		error=true;
	    errmsg += "<div class='error'>Please indicate the political party you most identify with</div>";
	    $('#error-2').html(errmsg);
	    $("#GetPol-wrapper").addClass("error"); 
	}
	else
	{ 

		if(party=="independent")
		{
		    var pform1="Independent";
		    var pform2="Independents";
		    
		}
	    if(party=="democrat")
		{ 
		    var pform1="Democrat";
		    var pform2="Democrats";
		}
	    if(party=="republican")
		{ 
		    var pform1="Republican";
		    var pform2="Republicans";
		}
	    if(party=="constitution")
		{ 
		    var pform1="Constitution Party member";
		    var pform2="Constitution Party members";
		}
	    if(party=="green")
		{ 
		    var pform1="Green Party member";
		    var pform2="Green Party members";
		}
	    if(party=="libertarian")
		{
		    var pform1="Libertarian";
		    var pform2="Libertarians";

		}

	
	    twitid = $("#twitid").html();
	    $("#GetPol-wrapper").hide(500); 
	    $("#politics_h").hide();

	    //$("#full-saspect").show();
	    displayQ(pform1, pform2, "party");
	    $.post("core/DataWrangler.php", {"page":"polform", "twitid":twitid, "party":party });



	}// end if that this embedded in the else

	}// End else
} // End the checkPolitics function




function displayQ(form1, form2, iden) // added iden as the third input
{	
    var i;
    
    //var clear = ''
    //$("displayQ-wrapper").html(clear);// reset the display wrapper so it doesn't store previous questions. 

    var wrapper = "#displayQ-wrapper_" + iden; // There is a different wrapper for each survey type.
    var sent = []; 
    form2_c= capitalize(form2);
	

	    var sent = new Array();
	    sent.push('I feel a bond with ' + form2);
	    sent.push('I feel solidarity with ' + form2);
	    sent.push('I feel committed to ' + form2);
	    sent.push('I am glad to be a ' + form1);
	    sent.push('I think that ' + form2 + ' have a lot to be proud of');
	    sent.push('It is pleasant to be a ' + form1);
	    sent.push('Being a ' + form1 + ' gives me a good feeling');
	    sent.push('I often think about the fact that I am a ' + form1);
	    sent.push('The fact that I am a ' + form1 + ' is an important part of my identity');
	    sent.push('Being a ' + form1 + ' is an important part of how I see myself');
	    sent.push('I have a lot in common with the average ' + form1);
	    sent.push('I am similar to the average ' + form1); // This one is modified slightly
	    sent.push(form2_c + ' have a lot in common with each other');
	    sent.push(form2_c + ' are very similar to each other');



	
	for(i=0; i<sent.length; i++)
	{
	    likert = createLikert( iden + 'likert_' + i, iden + '_agree_' + i);
	
	    // $("divname").css('color','red');

	    $(wrapper).append('<div> <li id = "err'+ iden + i + '">' + sent[i]  + '</li> <p>' + likert + '</p></div>');
	    //$("#displayQ-wrapper").append('<li>'+ sent[i]  + '</li><p>' + likert + '</p>');
	}

	$(wrapper).shuffle(); 
	$(wrapper).append('<div id="error'+ iden +'" class="error"/>'); // appends a unique error id for each section

	
	// put the code for where the error message will go above the button
	
	
	//$("#displayQ-wrapper").append('<div> <input type="button" value="Continue" onclick = "surveyValidate(\'' + iden +'\')"/></div>'); 

	$(wrapper).append('<p><input type="reset" id="fin_pol_likert" value="Continue"/></p>');

	//PolValidation(); 
	$(wrapper).show();


	$("#fin_pol_likert").click(function() {


		surveyValidate("party");
		
	

	});

	//$("#full-saspect").show();

		
}// end displayQ function


	function surveyValidate(iden)// added iden as an input
{
	console.log("it's getting to validate function")
	var j = 0;
	var error= false; 
	
	//var errmsg= ''; 
	//var error3= '<div id="error'+ iden +'" class="error"/>'	
	// $("displayQ").children("div").each(function(index) {
	//	errmsg += '<p> Please provide an answer to question ' + index + '</p>';
	// });

	var qdata = {};
	for(i=0; i <= 13; i++)
	{
	    //j += 1; 

	    var intermed= iden + '_agree_' + i ; // Used iden to fill in the pre-fix
	    qput= 'input[name = ' + intermed + ']:checked';
	    Q_input = $(qput).val();

	    var wrapper = "#displayQ-wrapper_" + iden;

	    //Q_input= $('input[name=pol_agree_+i]:checked').val(); 

	    if(Q_input == null)
		{
		    var errorid = '#err' + iden + i; 
		    error = true;
		    $(errorid).css('color','#F00'); 
		}
	    else
		{
		    qdata[iden + i] = Q_input;
		}
	}

	/*
	  if(error==true)
	  {
		$('#error'+ iden).html(errmsg); 
	  } 
	*/
	
	
	if(error==false || once == true)
	{   
	    twitid = $("#twitid").html();
	    $.post("core/DataWrangler.php", {"page":iden, "twitid":twitid, "data":qdata});
	    $(wrapper).hide(500); 
		once = false;

	   
		$("#politics_h").hide();
		//$("#full-saspect").show()
	

		$("#free_h").show();
	    $("#FreeForm-wrapper").show(500);


		    
		


	} 
		 
	   
	
	
	else
	{ 
	    $('#error'+ iden).html('Oops. We noticed you left one or more items blank (shown in red above). Your responses are most useful to us when you answer every question, so we would appreciate it if you fill those in. But if you choose not to answer those specific items, you can press "Continue" to move on'); 
	once = true;
	
	}
	
	
	

}// end surveyValidate()


	    $("#fin_free").click(function() 

	    {
	    	FreeCheck();
	    	
	    });	




function FreeCheck()
{ 
    nform1 = $("#free1").val();
    nform2 = $("#free2").val();
    userURL = $("#user_url").val();
	nform3 = $("#free3").val();
	nform4 = $("#free4").val();
	userURL2 = $("#user_url2").val();
	nform5 = $("#free5").val();
	nform6 = $("#free6").val();
	userURL3 = $("#user_url3").val();
	
	
    errmsg = '<p> Oops. Though all questions are optional and you may proceed at any time, it would be really helpful if you provide answers to these items. </p>';

    //alert(nform1 + ", " + nform2 + ", " + validURL(userURL));
	
    //nform1 = capitalize(nform1) 
    //nform2 = capitalize(nform2)
	
    //nform1 = nform1.charAt(0).toUpperCase() + nform1.slice(1);
    //nform2 = nform2.charAt(0).toUpperCase() + nform1.slice(1); 
    
	
	
    error = false;
	

    if(nform1.length < 3)
	{ 
	    error = true;
	    errmsg += '<p> Please provide an appropriate answer to item 1, shown in red above </p>';
	    
	    //$("#freeq1").addClass("error")
	    $("#freeq1").css('color','red');
	    
	}// add more to this later
	else
	{
		$("#freeq1").css('color','black');
		
	} 

    if(nform2.length < 3)
	{ 
	    error = true;
	    errmsg += '<p> Please provide an appropriate answer to item 2 </p>';
	    //$("#freeq2").addClass("error")
	    $("#freeq2").css('color','red');
	}
	else
	{
		$("#freeq2").css('color','black');
		
	} 
    if(!validURL(userURL))
	{ 
	    error = true;
	    errmsg += '<p> Please provide a valid URL </p>';
	    //$("#freeq2").addClass("error")
	    $("#freeq3").css('color','red');
	}  
	else
	{
		$("#freeq3").css('color','black');
		
	} 
	
	  if(error== false || once == true)
	{   once = false
	    twitid = $("#twitid").html();
	    $.post("core/DataWrangler.php", {"page":"freeform", "twitid":twitid, "data":{"ownform1":nform1,"ownform2":nform2, "ownURL":userURL, "ownform3":nform3, "ownform4":nform4, "ownURL2":userURL2, "ownform5":nform5, "ownform6":nform6, "ownURL3":userURL3} });
	    $("#FreeForm-wrapper").hide(500);
		$("#free_h").hide(); 
		$("#full-saspect").show();
		
		

	}  
    else
	{
	    $("#error-5").html(errmsg);
		once = true
	}
  
}// End free check



	//$("#full-saspect").show();


	for (var i = 0; i < traits_full.length; i++) // Here we are creating the buttons for the traits
	{
    	
		button_str =  '<small>';
		button_str +=  '<input id="'+traits_full[i];
		button_str +=  '" class = "trait_buttons" type="checkbox" checked="unchecked" />';
		button_str +=  ' <label for="'+traits_full[i]+'">'+traits_full[i]+'</label>';
		button_str += '</small>'

		$("#trait_buttons").append(button_str);

		$("[id='"+traits_full[i]+"']").button();

	}


function validURL(userURL){
    return /^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$/.test(userURL);
    //    return /((http|https):\/\/(\w+:{0,1}\w*@)?(\S+)|)(:[0-9]+)?(\/|\/([\w#!:.?+=&%@!\-\/]))?/.test(userURL);
}

function capitalize(string)
{
    return string.charAt(0).toUpperCase() + string.slice(1);	
}

function createLikert(id_label,name_label)
{
	var likert = '<table class="likert"><tr><td><input id="' + id_label +
	'" type="radio" name="' + name_label + 
	'" value="1" /></td><td><input type="radio" name="' + name_label + 
	'" value="2" /></td><td><input type="radio" name="' + name_label + 
	'" value="3" /></td><td><input type="radio" name="' + name_label + 
	'" value="4" /></td><td><input type="radio" name="' + name_label + 
	'" value="5" /></td><td><input type="radio" name="' + name_label + 
	'" value="6" /></td><td><input type="radio" id="' + id_label + 
	'" name="' + name_label + 
	'" value="7" /></td></tr>' +
	'<tr><td>Strongly Disagree</td>' +
	'<td></td>' +
	'<td></td>' +
	'<td></td>' +
	'<td></td>' +
	'<td></td>' +
	'<td>Strongly Agree</td></tr></table>';

	return likert;
}



//$("#full-saspect").show();

 //Disp_Self_Lab(); 

 
	//$("#trait_buttons").show();

	//$('.trait_disp').show()
	
	

	$(".trait_buttons").click(function() {	

		if($.inArray(this.id, traits_arr) == -1 ) // if a the trait associated with the button (this.id) is not in the current trait array, do the following:
		{
		 
			console.log(traits_arr.push(this.id));
			$('#traits_show').append('<div id= "disp_'+this.id+'" class="t_disp">'+this.id+'</div>');
		
		} 
		else
		{
			var removeItem = $(this).attr("id"); // if the trait is in the array, then this means someone is trying to remove it, this piece pulls the item string name.

			traits_arr = jQuery.grep(traits_arr, function(value) { // creates a new copy of the array with the item removed
		 		return value != removeItem;
			});

			var j= "[id='disp_" // putting together the string that will be used as the selector using variables j,k,l

			var k=$(this).attr("id")

			var l="']"


			toremove=j+k+l;

			$(toremove).remove();
			
	 	}
	
	}); // ends trait_buttons click function

	//console.log(traits_arr)

	$("#add_group").click(function() {   
		//console.log(traits_arr)
		
		var string_name=$("#Self-Name").val();
		
		
		if(traits_arr.length > 0 && $.trim(string_name).length > 2 ) //
		{
			
			var labelname = $("#Self-Name").val();
			var traits_temp= traits_arr.join();
			var diff_variable=traits_arr.join();
			
			if(edit==false)
			{
				var trait_group = '<div class = "self_finished" id="self_display_'+self_count+'">';
				trait_group += ' Self-Aspect '+self_count+': '+labelname;
				trait_group += ' <br> Traits: '+traits_temp;
				trait_group += ' <br><button  class="edit_button" value="'+self_count+'"> edit </button>';
				trait_group += '</div>';
				$("#right_side").append(trait_group);
				
				var h= self_count;
				
				self_count += 1;

				
			}			
			else
			{
				var id_tofill = "#self_display_"+current_count;

				var trait_edit = 'Self-Aspect '+current_count+': '+labelname;
				trait_edit += ' <br> Traits: '+diff_variable;
				trait_edit += ' <br><button  class="edit_button" value="'+current_count+'"> edit </button>';

				$(id_tofill).html(trait_edit);
				$(id_tofill).show();
				
				console.log("conditional in place")
				
				edit=false // importantly once the trait has been added, it is no longer being edited, so the value of this variable much false. Otherwise people won't be able to create new
				// groups after this. 	

				var h= current_count;						
			}
			
			

		     //traits_arr=[]
			//console.log(diff_variable);
			//$(traits_show).empty();//I don't think this is doing anything
			
			

			var curr_self_aspect= 'self_aspect'+h;
			var traits_curr= 'Traits' + h;
			
	        dic_self[curr_self_aspect]=$("#Self-Name").val();
			//console.log(trait_dic2['self_aspect1'])
			dic_trait[traits_curr]=traits_arr;
			console.log(dic_trait['Traits1']);
			
			$("#Self-Name").val("");
			
	
			var traits_copy = traits_arr; // it's important to creat a full copy of traits_arr (the working set of traits that is being edited, because every click it will be adjusted
			// so iterating through this is like iterating through a moving changing target. Items will get skipped. So, in the below code, I iterate through traits_copy, not traits_arr because
			// the loop impacts it on the fly. 

			for(var i = 0; i < traits_copy.length; i++) 
			{   console.log("it is looping")
				
				$("[id='"+traits_copy[i]+"']").click();	

			}

			
			// I can put an else statement here that informs the participant that they must add Both traits and a
			// trait name before in order to add the group. 
			
			
		} // this is actually the end of the if statement
		else
		{ console.log("it's working here yo")
			$("#dialogue_add_group").dialog({
				title: 'Incomplete Information',
				  width: 500,
				  height: 200,
				  modal: true,
				  resizable: false,
				  draggable: false,
			})
				  
				 
			
			
		}
		
		
		function edit_piece() // This is the code that should be run when nothing is stored in the current editor and the participant wants to edit an entry.
			{
				edit=true;

			//var j='#self_display_'+current_count;
					//console.log(j);

					//$(j).hide()
			

			// hide the current piece that is being edited


			
			
			console.log(current_count);
			
			var current_trait='Traits'+current_count;
			var current_aspect='self_aspect'+current_count;
			
			console.log(current_aspect);

			var id_tofill = "#self_display_"+current_count;

			$(id_tofill).hide();
			
			
			var cur_trait_arr=dic_trait[current_trait]; // Variable for the trait set
			var cur_aspect_label=dic_self[current_aspect];
			
			console.log(cur_trait_arr);
			
			for(var i = 0; i < cur_trait_arr.length; i++)
			{
				$("[id='"+cur_trait_arr[i]+"']").click();		
			}
			$("#Self-Name").val(cur_aspect_label);


			}
		//|| $.trim(string_name).length > 2
		
		// Here is the click function for the edit button

		$(".edit_button").click(function()

		{
			console.log("The click is working");
			
			var string_name=$("#Self-Name").val(); // just breaking this up into a string, which I will trim and take the length of to see if a self-aspect name is long enough
			
			current_count= parseInt($(this).attr("value")); // 

		  
			
			if(traits_arr.length>0){ // If someone has 
			$('#dialog_box').dialog({
			
				  title: 'Unsaved Self-Aspect',
				  width: 500,
				  height: 400,
				  modal: true,
				  resizable: false,
				  draggable: false,
				  buttons: [{
				  text: 'Yes',
				  click: function()
				  {   $(this).dialog('close')
					  var traits_copy = traits_arr;
					  for(var i = 0; i < traits_copy.length; i++) 
						{
				
							$("[id='"+traits_copy[i]+"']").click();	

						} 


					edit_piece(); // 
					 
					
				   }//end click button function
			    }, // end of first button argument
				
				
				  { 
				  text: 'No',
				  click: function() {
					  $(this).dialog('close');
					}
				  }]
				});
			}
			
			else
			 {
				edit_piece();
				
			}
			

		}); // ends the edit button click function
			
		
	}); // ends the add group click function


  $("#finish_SA").click(function()
     {
     	// make this a validation function

     	if(Object.keys(dic_self).length==0 && once==false)

     	{	once=true;
     		$("#right_col").append('<div id="error_sa_list" class= "error"> Oops, looks like you did not add a self-aspect. It would help us greatly if you include one.</div>')
     	
     		//$("#right-col").show();

     	}


     	else{



     	
       $("#full-saspect").hide(500);
       once=false;

       if(Object.keys(dic_self).length==0)// if someone didn't input a self aspect, skip the next section. 
       {
       Show_media_qs();


       }
       else
       {

            Disp_Self_Lab(); // only display the next section of labeling self-aspects if people have input a self aspect
  		}
      } // end super-ordinate else

     });// end click function



function Disp_Self_Lab()// Function to initiate the self-labeling portion of the study. 

{
	var dropdown=
['<p>',
	'<select id="self_categories" name="edu">', 
		'<option value="unselected" selected="selected"></option>',
		'<option value="situations">Situations</option>',
		'<option value="relationships">Relationships</option>',
		'<option value="roles">Roles</option>',
		'<option value="emotional">Emotional</option>',
		'<option value="true_selves">True Selves</option>',
		'<option value="goals">Goals</option>',
		'<option value="time">Time Related</option>',
		'<option value="public">Public</option>',
		'<option value="alone">Alone</option>',
		'<option value="other">Other</option>',
	'</select>',
'</p>' 
].join('\n')

var Qsappend="";// these are questions that will be appended at that end

var sent_base1='From the dropdown menu, choose the category, listed above, that best describes the following Self-Aspect: "';

$.each(dic_self, function(key, value) {
	var item_temp='<p><label for = "part_label_'+key+'"><b>'+ sent_base1 + value + '".</b></label><br>' + dropdown + '</p>';
	Qsappend += item_temp;

    	
    		});

	Qsappend +='<p><input type=reset id ="finish_label" value= "Submit" /></p>'

	$("#self_labeling").append(Qsappend)
	$("#self_labeling").show()

    $("#finish_label").click(function()
     {
     	// make this a validation function

     //console.log("click working")
       

     //Show_media_qs(); 

     ShowGenaspect();

     });

}   

   function ShowGenaspect()// This function just asks people about the clarity, importance and positivity of the self-aspects they listed
	   {  	

	   	$("#self_labeling").hide(); 
	   	function createLikertS1(id_label,name_label)// I'm making three of these because the scales are all a little different. 
		{
			var likert = '<table class="likert"><tr><td><input id="' + id_label +
			'" type="radio" name="' + name_label + 
			'" value="1" /></td><td><input type="radio" name="' + name_label + 
			'" value="2" /></td><td><input type="radio" name="' + name_label + 
			'" value="3" /></td><td><input type="radio" name="' + name_label + 
			'" value="4" /></td><td><input type="radio" name="' + name_label + 
			'" value="5" /></td><td><input type="radio" name="' + name_label + 
			'" value="6" /></td><td><input type="radio" name="' + name_label + 
			'" value="7" /></td></tr>' +
			'<tr><td>Negatively</td>' +
			'<td></td>' +
			'<td></td>' +
			'<td>Neutral</td>' +
			'<td></td>' +
			'<td></td>' +
			'<td>Positively</td></tr></table>';

			return likert;
		}


		function createLikertS2(id_label,name_label)// I'm making three of these because the scales are all a little different. 
		{
			var likert = '<table class="likert"><tr><td><input id="' + id_label +
			'" type="radio" name="' + name_label + 
			'" value="1" /></td><td><input type="radio" name="' + name_label + 
			'" value="2" /></td><td><input type="radio" name="' + name_label + 
			'" value="3" /></td><td><input type="radio" name="' + name_label + 
			'" value="4" /></td><td><input type="radio" name="' + name_label + 
			'" value="5" /></td><td><input type="radio" name="' + name_label + 
			'" value="6" /></td><td><input type="radio" name="' + name_label + 
			'" value="7" /></td></tr>' +
			'<tr><td>Not At All Important</td>' +
			'<td></td>' +
			'<td></td>' +
			'<td></td>' +
			'<td></td>' +
			'<td></td>' +
			'<td>Very Important</td></tr></table>';

			return likert;
		}

		function createLikertS3(id_label,name_label)// I'm making three of these because the scales are all a little different. 
		{
			var likert = '<table class="likert"><tr><td><input id="' + id_label +
			'" type="radio" name="' + name_label + 
			'" value="1" /></td><td><input type="radio" name="' + name_label + 
			'" value="2" /></td><td><input type="radio" name="' + name_label + 
			'" value="3" /></td><td><input type="radio" name="' + name_label + 
			'" value="4" /></td><td><input type="radio" name="' + name_label + 
			'" value="5" /></td><td><input type="radio" name="' + name_label + 
			'" value="6" /></td><td><input type="radio" name="' + name_label + 
			'" value="7" /></td></tr>' +
			'<tr><td>Not At All Clear</td>' +
			'<td></td>' +
			'<td></td>' +
			'<td></td>' +
			'<td></td>' +
			'<td></td>' +
			'<td>Very Clear</td></tr></table>';

			return likert;
		}

		

		//Get the self-aspects

		var self_aspect=[]// initialize array that will contain self-aspects

		$.each(dic_self, function(key, value) {
		
		
		self_aspect.push(value)

    	
    		});

		// There are 3 for loops when there only needs to be one- change later after flow is complete. It is clunky, but
		// at least it works for now. 

		var wrapper='#Self_Q1'

		//First make the sentences that use scale 1 for all aspects

			for(i=0; i<self_aspect.length; i++)
			{
			    likert = createLikertS1( 'Self_Q1_' + i, 'pos' + i);


			    $('#Self_Q1').append('<div= "sen_pos'  + i + '">How positive do you feel about "' + self_aspect[i] + '"?<p>' + likert + '</p></div>');
			    //$("#displayQ-wrapper").append('<li>'+ sent[i]  + '</li><p>' + likert + '</p>');
			}

			$(wrapper).shuffle(); 
		    $(wrapper).show();



		    var wrapper='#Self_Q2'

		//Now make sentences that use scale 2

			for(i=0; i<self_aspect.length; i++)
			{
			    likert = createLikertS2( 'Self_Q2_' + i, 'import' + i);

			    $('#Self_Q2').append('<div= "sen_import'  + i + '">How important is "' + self_aspect[i] + '" to you?<p>' + likert + '</p></div>');
			    
			}

			$(wrapper).shuffle(); 
		    $(wrapper).show();


		     var wrapper='#Self_Q3'

		//Now make sentences that use scale 2

			for(i=0; i<self_aspect.length; i++)
			{
			    likert = createLikertS3( 'Self_Q3_' + i, 'clear' + i);

			    $('#Self_Q3').append('<div= "sen_clear'  + i + '">How clear is "' + self_aspect[i] + '" to you?<p>' + likert + '</p></div>');
			    
			}

			$(wrapper).shuffle(); 
		    $(wrapper).show();

		    $("#all_genself").append('<p><input type=reset id ="finish_genself" value= "Submit" /></p>')


		     $("#finish_genself").click(function()
			     {
			     	 
			     	Show_media_qs(); 


			     });
		

	   }// End show general questions function


	function Show_media_qs() //asks specific questions about social media usage. 
	{    $("#all_genself").hide();

		function Likert_Social(id_label,name_label)
			{
				var likert = '<table class="likert"><tr><td><input id="' + id_label +
				'" type="radio" name="' + name_label + 
				'" value="1" /></td><td><input type="radio" name="' + name_label + 
				'" value="2" /></td><td><input type="radio" name="' + name_label + 
				'" value="3" /></td><td><input type="radio" name="' + name_label + 
				'" value="4" /></td><td><input type="radio" name="' + name_label + 
				'" value="5" /></td><td><input type="radio" name="' + name_label + 
				'" value="6" /></td><td><input type="radio" name="' + name_label + 
				'" value="7" /></td></tr>' +
				'<tr><td>Never</td>' +
				'<td></td>' +
				'<td></td>' +
				'<td></td>' +
				'<td></td>' +
				'<td></td>' +
				'<td>Always</td></tr></table>';

				return likert;
			}


		$.each(dic_self, function(key, value) // make facebook questions to put in facebook_saspect wrapper
		{

			likertFB = Likert_Social( 'Sfb_likert_' + key, 'Sfb_agree_' + key);
			likertTW = Likert_Social( 'Stw_likert_' + key, 'Stw_agree_' + key);


			var id1="self_fb"+i
		    var name1="self_fbname"+i
		    var id2="self_tw"+i
		    var name2="self_twname"+i

		    var comment1='<p> Add Comment <textarea id="'+id1+'"cols="50" rows="1" name="'+name1+'"></textarea></p>';

		    var comment2='<p> Add Comment <textarea id="'+id2+'"cols="50" rows="1" name="'+name2+'"></textarea></p>';
	


	    senForpop="How often do you express "

	    $('#PopFB').append('<div id = "fbfreq_'  + key + '">' + senForpop + '"' + value + '" on Facebook? <p>' + likertFB + '</p>'+comment1+'</div>');
	    //Maybe I should mix all the facebook questions together- the ones populated and the ones not populated. Append and then
	    // shuffle them at the end. 
		
		$('#PopTwitter').append('<div id = "twfreq_'  + key + '">' + senForpop + '"'+ value + '" on Twitter? <p>' + likertTW + '</p>'+comment2+'</div>');


			});


		var sen_FB = new Array();// Sentences for facebook questions
		sen_FB.push("On Facebook how often do you express how you are feeling at the moment?")
		sen_FB.push("On Facebook how frequently do you express what you are doing?")
		sen_FB.push("On Facebook how often do you express where you are?")
		sen_FB.push("On Facebook how often do you express things that are not about your own feelings\
\n(or what you're doing or where you are), but that you expect to interest or entertain others?")
		sen_FB.push("On Facebook how often do you express things of a political nature?")
		sen_FB.push("On Facebook how often do you express things related to your relationship with family?")
		sen_FB.push("On Facebook how often do you express things related to God?")
		sen_FB.push("On Facebook how often do you express things related to your academic life?")
		sen_FB.push("On Facebook how often do you express things related to your physical appearance?")




		



		var sen_Twitter = new Array();//sentences for twitter questions

		sen_Twitter.push("On Twitter how often do you express how you are feeling at the moment?")
		sen_Twitter.push("On Twitter how frequently do you express what you are doing?")
		sen_Twitter.push("On Twitter how often do you express where you are?")
		sen_Twitter.push("On Twitter how often do you express things that are not about your own feelings\
\n(or what you're doing or where you are), but that you expect to interest or entertain others?")
		sen_Twitter.push("On Twitter how often do you express things of a political nature?")
		sen_Twitter.push("On Twitter how often do you express things related to your relationship with family?")
		sen_Twitter.push("On Twitter how often do you express things related to God?")
		sen_Twitter.push("On Twitter how often do you express things related to your academic life?")
		sen_Twitter.push("On Twitter how often do you express things related to your physical appearance?")
		for(i=0; i<sen_FB.length; i++)
			{
		    likert1 = Likert_Social( 'fb_likert_' + i, 'fb_agree_' + i);

		    likert2 = Likert_Social( 'tw_likert_' + i, 'tw_agree_' + i);
		
		    		    //adding place where people can comment

		    var id1="com_fb"+i
		    var name1="com_fbname"+i
		    var id2="com_tw"+i
		    var name2="com_twname"+i

		    var comment1='<p> Add Comment <textarea id="'+id1+'"cols="50" rows="1" name="'+name1+'"></textarea></p>';

		    var comment2='<p> Add Comment <textarea id="'+id2+'"cols="50" rows="1" name="'+name2+'"></textarea></p>';

		    $('#PopFB').append('<div = "err_fbfreq'  + i + '">' + sen_FB[i]  + '<p>' + likert1 + '</p>'+comment1+'</div>');
		    $('#PopTwitter').append('<div= "err_twfreq' + i + '">' + sen_Twitter[i]  + '<p>' + likert2 + '</p>'+comment2+'</div>');
		    
			}

		$('#PopFB').shuffle(); // Randomize the order of the FB questions
		$('#PopTwitter').shuffle();

		$('#facebookQs').append('<p><input type=reset id ="finish_fbQs" value= "Submit" /></p>')
		$("#twitterQs").append('<p><input type=reset id ="finish_twQs" value= "Submit" /></p>')


		$('#facebookQs').show(); 

		//$("#facebookQs").show();
		//$("#PopTwitter").show();

		$("#finish_fbQs").click(function()
			     {
			     	$('#facebookQs').hide(500);
			     	$("#twitterQs").show(500);
			     
			     	
			     });




		$("#finish_twQs").click(function()
			     {
			     	$('#twitterQs').hide();
			     	Show_CSW();
			     });

	}// End of show social media function


	function Show_CSW() // This function is particulary rough and dirty- It involves way more code than is necessary- but works
	// I will change it later, though out of principle. 
	{


		 var sen_con = new Array();// Just start by creating an array with all the sentences.

		 sen_con.push('When I think I look attractive, I feel good about myself.');
		 sen_con.push("My self-worth is based on God's love.");
		 sen_con.push("I feel worthwhile when I perform better than others on a task or skill.");
		 sen_con.push("My self-esteem is unrelated to how I feel about the way my body looks.");
		 sen_con.push('Doing something I know is wrong makes me lose my self-respect.');
		 sen_con.push("I don't care if other people have a negative opinion of me.");
		 sen_con.push("Knowing that my family members love me makes me feel good about myself.");
		 sen_con.push("I feel worthwhile when I have God's love.");
		 sen_con.push("I can't respect myself if other's don't respect me.");
		 sen_con.push("My self-worth is not influenced by the quality of my relationship with my family members.");
		 sen_con.push("Whenever I follow my moral principles, my sense of self-respect gets a boost.");
		 sen_con.push("Knowing that I am better than others on a task raises my self-esteem.");
		 sen_con.push("My opinion about myself isn't tied to how well I do in school.");
		 sen_con.push("I couldn't respect myself if I didn't live up to a moral code.");
		 sen_con.push("I don't care what other people think of me.");
		 sen_con.push("When my family members are proud of me, my sense of self-worth increases.");
		 sen_con.push("My self-esteem is influenced by how attractive I think my face or facial features are.");
		 sen_con.push("My self-esteem would suffer if I didn't have God's love.");
		 sen_con.push("Doing well in school gives me a sense of self-respect.");
		 sen_con.push("Doing better than others gives me a sense of self-respect.");
		 sen_con.push("My sense of self-worth suffers whenever I think I don't look good.");
		 sen_con.push("I feel better about myself when I know I'm doing well academically.");
		 sen_con.push("What others think of me has no effect on what I think about myself.");
		 sen_con.push("When I don't feel loved by my family my self-esteem goes down.");
		 sen_con.push("My self-worth is affected by how well I do when I am competing with others.");
		 sen_con.push("My self-esteem goes up when I feel that God loves me.");
		 sen_con.push("My self-esteem is influenced by my academic performance.");
		 sen_con.push("My self-esteem would suffer if I did something unethical.");
		 sen_con.push("It is important to my self-esteem that I have a family who cares about me.");
		 sen_con.push("My self-esteem does not depend on whether or not I feel attractive.");
		 sen_con.push("When I think that I'm disobeying God, I feel bad about myself.");
		 sen_con.push("My self-worth is influenced by how well I do on competetive tasks.");
		 sen_con.push("I feel bad about myself whenever my academic performance is lacking.");
		 sen_con.push("My self-esteem depends on whether or not I follow my moral/ethical principles.");
		 sen_con.push("My self-esteem depends on the opinions of others.");


 // Make some kind of wrapper called contingencies




		function create_cont_Likert(sentence,name_label)
		{    //console.log("it's getting here")
			var likert = '<tr><td style="text-align: left; height: 40px"> <b>' + sentence + '</b></td>'+
			'<td><input type="radio" name="' + name_label+ 
			'" value="1" /></td><td><input type="radio" name="' + name_label + 
			'" value="2" /></td><td><input type="radio" name="' + name_label + 
			'" value="3" /></td><td><input type="radio" name="' + name_label + 
			'" value="4" /></td><td><input type="radio" name="' + name_label + 
			'" value="5" /></td><td><input type="radio" name="' + name_label + 
			'" value="6" /></td><td><input type="radio" name="' + name_label + 
			'" value="7" /></td></tr>';

			return likert;
		}




	    function makeset1() //simple function that returns a string the contexts of which are appended to a wrapper
	    // which show the the first 12 multiple choice items for contingencies of self-worth. 

	    {	j=""// initiate a string that will be built up to represent the html that will be displayed. 


			for(var i = 0; i < 12; i++) // go throug the first 12 sentences
			{
			
				var temp=create_cont_Likert(sen_con[i],"con_agree_"+i); // this takes in our sentence and puts it with a corresponding
				// name the radio buttons (each sentence has a unique associated name for its radio buttons)

				j=j+temp;		

			}

			return j;

		}


		 function makeset2() // Next Set. Later will make all three of these one function, using an array and
		    // and join technique. This will be less code and cleaner. But for now I'm going with this to get the flow. 

	    	{	
	    		j=""// initiate a string that will be built up to represent the html that will be displayed. 


				for(var i = 12; i < 24 ; i++) // go throug the first 12 sentences
				{
				
					var temp=create_cont_Likert(sen_con[i],"con_agree_"+i); // this takes in our sentence and puts it with a corresponding
					// name the radio buttons (each sentence has a unique associated name for its radio buttons)

					j=j+temp;		

				}

			return j;

		}


		function makeset3() // last set

	    {	j=""// initiate a string that will be built up to represent the html that will be displayed. 


			for(var i = 24; i < 35 ; i++) // go through the first 12 sentences
			{
			
				var temp=create_cont_Likert(sen_con[i],"con_agree_"+i); // this takes in our sentence and puts it with a corresponding
				// name the radio buttons (each sentence has a unique associated name for its radio buttons)

				j=j+temp;		

			}

			return j;

		}

		var w=makeset1();
		var x=makeset2();
		var y=makeset3();



		$('#con_table1').append(w);
		$("#contingencies1").append('<p><input type=reset id ="finish_CSW1" value= "Submit" /></p>')

		$('#con_table2').append(w);
		$("#contingencies2").append('<p><input type=reset id ="finish_CSW2" value= "Submit" /></p>')

		$('#con_table3').append(y);
		$("#contingencies3").append('<p><input type=reset id ="finish_CSW3" value= "Submit" /></p>')
	 
		$('#contingencies1').show(); // start the flow for this set now that the other wrapper pieces have been created.

		$("#finish_CSW1").click(function()
		{
	     	$("#contingencies1").hide(500);
	     	
	     	$("#contingencies2").show(500);
		 });

		$("#finish_CSW2").click(function()
		{
	     	$("#contingencies2").hide(500);
	     	
	     	$("#contingencies3").show(500);
		 });

		$("#finish_CSW3").click(function()
		{
	     	$("#contingencies3").hide(500);
	     	
	     	DoPANAS();
		 });


	}//End ShowCSW function

	function DoPANAS()
	{


		var emotion=["interested","distressed","excited","upset","strong","guilty","scared","hostile","enthusiastic","proud",
		"tired","irritable","alert","ashamed","inspired","nervous","determined","attentive","jittery","active","afraid"]
		function PANAS_Likert(sentence,name_label)
		{    console.log("it's getting here")
			var likert = '<tr><td style="text-align: left; height: 40px"> <b>' + sentence + '</b></td>'+
			'<td><input type="radio" name="' + name_label+ 
			'" value="1" /></td><td><input type="radio" name="' + name_label + 
			'" value="2" /></td><td><input type="radio" name="' + name_label + 
			'" value="3" /></td><td><input type="radio" name="' + name_label + 
			'" value="4" /></td><td><input type="radio" name="' + name_label + 
			'" value="5" /></td></tr>';

			return likert;
		}


	function makeset1() //just like in the previous functions for the CSWs- makes the first set 

	    {	j=""// initiate a string that will be built up to represent the html that will be displayed. 


			for(var i = 0; i < 11; i++) // go throug the first 11 emotions. 
			{
			
				var temp= PANAS_Likert(emotion[i], emotion[i]); // this takes in our sentence and puts it with a corresponding
				// name the radio buttons (each sentence has a unique associated name for its radio buttons)

				j=j+temp;	

			}

			return j; 

		}

		function makeset2() //just like in the previous functions for the CSWs- makes the first set 

	    {	j=""// initiate a string that will be built up to represent the html that will be displayed. 


			for(var i = 11; i < 21; i++) // go throug the first 11 emotions. 
			{
			
				var temp= PANAS_Likert(emotion[i], emotion[i]); // this takes in our sentence and puts it with a corresponding
				// name the radio buttons (each sentence has a unique associated name for its radio buttons)

				j=j+temp;	

			}

			return j; 

		}

		var w=makeset1();
		var x=makeset2();


		$("#PANAS_table1").append(w);
		$("#PANAS_scale1").append('<p><input type=reset id ="finish_PANAS1" value= "Submit" /></p>')


		$("#PANAS_table2").append(x);
		$("#PANAS_scale2").append('<p><input type=reset id ="finish_PANAS2" value= "Submit" /></p>')

		$("#PANAS_scale1").show();

			$("#finish_PANAS1").click(function()
			{
		     	$("#PANAS_scale1").hide(500);
		     	
		     	$("#PANAS_scale2").show(500);
			 });
			$("#finish_PANAS2").click(function()
			{
		     	$("#PANAS_scale2").hide(500);
		     	
				$("feedback_h").show()
		     	$("#GetFeedback-wrapper").show()
			 });

				$("#fin_feedback").click(function()
			{
		     	$("feedback_h").hide(500);
		     	$("#GetFeedback-wrapper").hide();
		     	$("#thanks").show(); 

		     });


	
	}


	





}); // end the on document ready function





 
/*


$(document).ready(function(){
	$("#serious").hide()
  $("button").click(function(){
    $("#serious").toggle();
  });
});















*/

