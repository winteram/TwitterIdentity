

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


	// add years to age question
	for(i=2000;i>1900;i--)
	{
		$("#age").append('<option value="'+i+'">'+i+'</option>');
	}


	//This part just displays the inital introduction

	$("#section-header-0").show(); 
	$("#instructions-wrapper").show();



	//This function is to proceed from the first intro page. 

	$("#fin_intro").click(function() {

	getDemographics()	
	


	});

		function getDemographics()
	{$("#section-header-0").hide();
		$("#instructions-wrapper").hide(500);
		$("#demographics_h").show();
		$("#demo-wrapper").show(500);
	}


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


	$("#fin_pol_likert").click(function() {
	console.log("dog")

	});



function checkPolitics()
{
	party =$("#affiliation option:selected").val();

	var error = false;
	var errmsg= "";
	var wrapper = "#displayQ-wrapper_" + "party";
	iden = "party";
	
	if(once == true)
	{
	    $("#GetPol-wrapper").hide(500); 
	    $.post("core/DataWrangler.php", {"page":"polform", "twitid":twitid, "party":party });

		

		
	}
	
	

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
	    displayQ(pform1, pform2, "party");
	    $.post("core/DataWrangler.php", {"page":"polform", "twitid":twitid, "party":party });

	}
}


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

	$("#displayQ-wrapper").append('<div id = "error3" class = "error"> </div>'); 
	// put the code for where the error message will go above the button
	
	
	//$("#displayQ-wrapper").append('<div> <input type="button" value="Continue" onclick = "surveyValidate(\'' + iden +'\')"/></div>'); 

	$("#GetPol-wrapper").hide(500); // might have to do some conditionals here with "iden" if the current wrapper is not hiding
	//$("#displayQ-wrapper").show(500);

	PolValidation(); 

		
}


   function PolValidation()

   {

   	$("#displayQ-wrapper_party").append('<input id="fin_lik_pol" type=reset value="Submit" />')
   	$('#displayQ-wrapper_party').show()

   	$("#fin_lik_pol").click(function() {


   		surveyValidate("party")
	
	});



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

	console.log("it's getting into likert")

	return likert;
}




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
	

		$("#free_h").show();
	    $("#FreeForm-wrapper").show(500);

	    $("#fin_free").click(function() 

	    {
	    	FreeCheck()
	    });	
		    
		


	} 
		 
	   
	
	
	else
	{ 
	    $('#error'+ iden).html('Oops. We noticed you left one or more items blank (shown in red above). Your responses are most useful to us when you answer every question, so we would appreciate it if you fill those in. But if you choose not to answer those specific items, you can press "Continue" to move on'); 
	once = true;
	
	}
	
	
	

}// end surveyValidate()


function validURL(userURL){
    return /^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$/.test(userURL);
    //    return /((http|https):\/\/(\w+:{0,1}\w*@)?(\S+)|)(:[0-9]+)?(\/|\/([\w#!:.?+=&%@!\-\/]))?/.test(userURL);
}


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
		Display_Self_List()
		

	}  
    else
	{
	    $("#error-5").html(errmsg);
		once = true
	}
  
}// End free check




	function Display_Self_List()// This will ininitate the task where participants list self aspects.

{ console.log("it's getting to displayselflist")

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

	console.log("and here")


 
	$("#left_self").show();

	$('#finish_SA_but').show();
	$('#right_side').show(); 
	

	console.log("and even here")


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
				

				
			}			
			else
			{
				var id_tofill = "#self_display_"+current_count;

				var trait_edit = 'Self-Aspect '+current_count+': '+labelname;
				trait_edit += ' <br> Traits: '+diff_variable;
				trait_edit += ' <br><button  class="edit_button" value="'+current_count+'"> edit </button>';

				$(id_tofill).html(trait_edit);
				
				console.log("conditional in place")
				
				edit=false // importantly once the trait has been added, it is no longer being edited, so the value of this variable much false. Otherwise people won't be able to create new
				// groups after this. 							
			}



			
			

		     //traits_arr=[]
			//console.log(diff_variable);
			$(traits_show).empty();//I don't think this is doing anything
			
			var h= self_count;

			var curr_self_aspect= 'self_aspect'+h;
			var traits_curr= 'Traits' + h;
			
	        dic_self[curr_self_aspect]=$("#Self-Name").val();
			//console.log(trait_dic2['self_aspect1'])
			dic_trait[traits_curr]=traits_arr;
			console.log(dic_trait['Traits1']);
			
			$("#Self-Name").val("");
			
			self_count += 1;
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
			
			
			
			console.log(current_count);
			
			var current_trait='Traits'+current_count;
			var current_aspect='self_aspect'+current_count;
			
			console.log(current_aspect);
			
			
			var cur_trait_arr=dic_trait[current_trait]; // Variable for the trait set
			var cur_aspect_label=dic_self[current_aspect];
			
			console.log(cur_trait_arr);
			
			for(var i = 0; i < cur_trait_arr.length; i++)
			{
				$("[id='"+cur_trait_arr[i]+"']").click();		
			}
			$("#Self-Name").val(cur_aspect_label);


			}
		
		
		// Here is the click function for the edit button

		$(".edit_button").click(function()

		{
			console.log("The click is working");
			
			var string_name=$("#Self-Name").val(); // just breaking this up into a string, which I will trim and take the length of to see if a self-aspect name is long enough
			
			current_count= parseInt($(this).attr("value")); // 
		  
			
			if(traits_arr.length>0 || $.trim(string_name).length > 2){ // If someone has 
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

     	
       $("#full-saspect").hide(500);

      Disp_Self_Lab(); 

     });

 


}// End Display_Self List


	function IsNumeric(input)
	{
		return (input - 0) == input && input.length > 0;
	}









	//Display_Self_List();
	
	

	







}); // end the on document ready function





 
/*


$(document).ready(function(){
	$("#serious").hide()
  $("button").click(function(){
    $("#serious").toggle();
  });
});















*/

