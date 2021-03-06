 var nationalities;
var finished = false;


$(document).ready(function() {
	// add years to age question
	for(i=2000;i>1900;i--)
	{
		$("#age").append('<option value="'+i+'">'+i+'</option>');
	}

	// Check if order already determined
	// Randomly assign order of survey questions
	if(Math.random() >= .5)
	    { order= 1}
	else
	    { order= 2}
		
	once = false;
		
		

	// verify they want to leave (if before ThankYou)
	$(window).bind('beforeunload', function() { if(!finished) { return 'Are you sure you want to leave? You will lose any progress you have made on the survey.';} }); 

 
	// show demographics questions at beginning
	$("#section-header-0").show(); 
	$("#instructions-wrapper").show();
	
	// initialize auto-complete for nationalities
	$.get("core/nationalities.csv", function(data) {
		nationalities = data.split(",");
		function split( val ) {
			return val.split( /,\s*/ );
		}
		function extractLast( term ) {
			return split( term ).pop();
		}
		$( "#national" )
			// don't navigate away from the field on tab when selecting an item
			.bind( "keydown", function( event ) {
				if ( event.keyCode === $.ui.keyCode.TAB &&
						$( this ).data( "autocomplete" ).menu.active ) {
					event.preventDefault();
				}
			})
			.autocomplete({
				minLength: 0,
				source: function( request, response ) {
					// delegate back to autocomplete, but extract the last term
					response( $.ui.autocomplete.filter(
						nationalities, extractLast( request.term ) ) );
				},
				focus: function() {
					// prevent value inserted on focus
					return false;
				},
				select: function( event, ui ) {
					var terms = split( this.value );
					// remove the current input
					terms.pop();
					// add the selected item
					terms.push( ui.item.value );
					// add placeholder to get the comma-and-space at the end
					terms.push( "" );
					this.value = terms.join( "," );
					return false;
				}
			});
	});
	
});

function getDemographics()
{$("#section-header-0").hide();
	$("#instructions-wrapper").hide(500);
	$("#demographics_h").show();
	$("#demo-wrapper").show(500);
}

function IsNumeric(input)
{
	return (input - 0) == input && input.length > 0;
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


//Insert political affiliation into sentences with the right noun form

function displayQ(form1, form2, iden) // added iden as the third input
{	
    var i;
    
    //var clear = ''
    //$("displayQ-wrapper").html(clear);// reset the display wrapper so it doesn't store previous questions. 

    var wrapper = "#displayQ-wrapper_" + iden; // There is a different wrapper for each survey type.
    var sent = []; 
	
    form2_c= capitalize(form2); // captilizes first letter, when necessary. 
    if(iden == "nation")
	{
	    var sent = new Array();
	    sent.push('I feel a bond with ' + form2);
	    sent.push('I feel solidarity with ' + form2);
	    sent.push('I feel committed to ' + form2);
	    sent.push('I am glad to be ' + form1);
	    sent.push('I think that ' + form2 + ' have a lot to be proud of');
	    sent.push('It is pleasant to be ' + form1);
	    sent.push('Being ' + form1 + ' gives me a good feeling');
	    sent.push('I often think about the fact that I am ' + form1);
	    sent.push('The fact that I am ' + form1 + ' is an important part of my identity');
	    sent.push('Being ' + form1 + ' is an important part of my identity');
	    sent.push('I have a lot in common with the average ' + form1);
	    sent.push('I am similar to the average ' + form1); // This one is modified slightly
	    sent.push(form2_c + ' have a lot in common with each other');
	    sent.push(form2_c + ' are very similar to each other');
	}

	
    else
	{
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
	}
	
	for(i=0; i<sent.length; i++)
	{
	    likert = createLikert( iden + 'likert_' + i, iden + '_agree_' + i);
	
	    // $("divname").css('color','red');

	    $(wrapper).append('<div> <li id = "err'+ iden + i + '">' + sent[i]  + '</li> <p>' + likert + '</p></div>');
	    //$("#displayQ-wrapper").append('<li>'+ sent[i]  + '</li><p>' + likert + '</p>');
	}

	$(wrapper).shuffle(); 
	$(wrapper).append('<div id="error'+ iden +'" class="error"/>'); // appends a unique error id for each section

	// $("#displayQ-wrapper").append('<div id = "error3" class = "error"> </div>'); 
	// put the code for where the error message will go above the button
	
	$(wrapper).append( '<input type="button" value="Continue" onclick = "surveyValidate(\'' + iden +'\')"/>');
	//$("#displayQ-wrapper").append('<div> <input type="button" value="Continue" onclick = "surveyValidate(\'' + iden +'\')"/></div>'); 

	$("#GetPol-wrapper").hide(500); // might have to do some conditionals here with "iden" if the current wrapper is not hiding
	//$("#displayQ-wrapper").show(500);

	$(wrapper).show(500);	
}

function surveyValidate(iden)// added iden as an input
{
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
		once = false

	    if(iden=="party")
		{   
		    $("#politics_h").hide();
		    if(order==1)
			{   
			    $("#nationality_h").show();
			    $("#Nation-wrapper").show(500);
			}
		    else
			{   
			    $("#free_h").show();
			    $("#FreeForm-wrapper").show(500); 
			}
		}
	    if(iden=="nation")
		{   
		    $("#nationality_h").hide();
		    if(order==1)
			{   
			    $("#free_h").show();
			    $("#FreeForm-wrapper").show(500);
			} 
		    else
			{   
			    $("#politics_h").show();
			    $("#GetPol-wrapper").show(500);
			}
		}
	   
	}
	
	else
	{ 
	    $('#error'+ iden).html('Oops. We noticed you left one or more items blank (shown in red above). Your responses are most useful to us when you answer every question, so we would appreciate it if you fill those in. But if you choose not to answer those specific items, you can press "Continue" to move on'); 
	once = true	 
	
	}
	
	
	

}



function Thanks()
{   
    finished = true;
	
    comments = $("#feedback").val();

    twitid = $("#twitid").html();
    $.post("core/DataWrangler.php", {"page":"comments", "twitid":twitid, "comments":comments });
	
    $("#feedback_h").hide();
    $("#GetFeedback-wrapper").hide(500);

    $("#thanks").show(500); 
	
}


// Need to insert other branches this use the "order" variable to determine sequences as wel 
function DecideOrder(location)
{

	/*if( location == 'us' || order== 1)
	  
	  {
	  $("#GetPol-wrapper").show(500);
	  }
	  else
	  {
	  $("#Nation-wrapper").show(500)
	  } 
	  $("#tester").append('<p> Show something please! <p>');
	  $("#tester").show(500);  */

    if(location == "us")
	{
	    if(order==1) 
		{    
		    $("#politics_h").show();
		    $("#GetPol-wrapper").show(500);
		}
	    else 
		{   
		    $("#nationality_h").show(); 
		    $("#Nation-wrapper").show(500);
		}
	} 
    else 
	{   
	    order=1;
	    $("#nationality_h").show(); 
	    $("#Nation-wrapper").show(500);
	}
} 






function checkPolitics()
{
	party =$("#affiliation option:selected").val();

	var error = false;
	var errmsg= "";
	

	if(party == "unselected")
	{ 
	    error=true;
	    errmsg += "<div class='error'>Please indicate the political party you most identify with</div>";
	    $('#error-2').html(errmsg);
	    $("#GetPol-wrapper").addClass("error"); 
	}
	else
	{ 
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

function capitalize(string)
{
    return string.charAt(0).toUpperCase() + string.slice(1);	
}

function CheckNationID()
{ 
    // take list of nations, split into array
    nation_list = $("#national").val().replace(/,+$/,'').split(',');
    nform1 = nation_list.join('-');
    
    n_end = nform1.slice(-1);
    n_ese= nform1.slice(-3);
    //n_ch= nform1.slice(-2);
	
	//("li").addClass("black")
	
    if(n_end == "s" || n_end == "x" || n_end == "z" || n_end =="h" || n_ese == "ese")
	{
	    nform2=nform1;
	}
	else 
	{
	    nform2 = nform1 + "s";
	}
	
    // create array of exceptions to 's' rule
    // check if last nation is exception
    // nform2 = nform1 + "s";
    errmsg='';

    var error = false;

    for( nation in nation_list )
	{
	    if($.inArray(nation_list[nation],nationalities)==-1)
		{
		    error = true;
		    errmsg += '<p class="error"> Oops. Please type your nationality to proceed.</p>'
		    $("#nationalityq").css('color','red'); 
		}
	}


	 if(error == false)
		{
			
			once = false
			twitid = $("#twitid").html();
			$.post("core/DataWrangler.php", {"page":"natform", "twitid":twitid, "nationality":nform1 });
			$("#Nation-wrapper").hide(500);
			displayQ(nform1,nform2,"nation");
			
		}
	
    else
	{   $("#nationalityq").css('color','red'); 
		$("#error-4").html(errmsg);
		once = true
		
	} 
    
}

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
	
	
    errmsg = '<p> Oops. Please provide information for at least one identity </p>';

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
		once = true
	    
	}// add more to this later
	else
	{
		$("#freeq1").css('color','black');
		
	} 

    if(nform2.length < 3)
	{ 
	    error = true;
	    errmsg += '<p> Please provide an appropriate answer to item 2, shown in red above </p>';
	    //$("#freeq2").addClass("error")
	    $("#freeq2").css('color','red');
		once = true
	}
	else
	{
		$("#freeq2").css('color','black');
		
	} 
    if(!validURL(userURL))
	{ 
	    error = true;
	    errmsg += '<p> Please provide a valid URL for the item shown in red above </p>';
	    //$("#freeq2").addClass("error")
	    $("#freeq3").css('color','red');
		once = true
	}  
	else
	{
		$("#freeq3").css('color','black');
		
	} 
	
	  if(error== false)
	{   once = false
	    twitid = $("#twitid").html();
	    $.post("core/DataWrangler.php", {"page":"freeform", "twitid":twitid, "data":{"ownform1":nform1,"ownform2":nform2, "ownURL":userURL, "ownform3":nform3, "ownform4":nform4, "ownURL2":userURL2, "ownform5":nform5, "ownform6":nform6, "ownURL3":userURL3} });
	    $("#FreeForm-wrapper").hide(500);
		$("#free_h").hide(); 
	    $("#feedback_h").show();
		 $("#GetFeedback-wrapper").show(500);
	}  
    else
	{
	    $("#error-5").html(errmsg);
		
	}
  
}

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
	    DecideOrder(loc);
		once = false

	}
    else
	{
	    $('#error-1').html('Oops. We noticed you left one or more items blank (shown in red above). Your responses are most useful to us when you answer every question, so we would appreciate it if you fill those in. But if you choose not to answer those specific items, you can press "Submit" to move on.');
		once = true
	}
	
}



