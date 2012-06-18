$(document).ready(function() {

	// add years to age question
	for(i=2000;i>1900;i--)
	{
		$("#age").append('<option value="'+i+'">'+i+'</option>');
	}


	if(Math.random() >= .5)// Randomly assign order of survey questions
	{ order= 1}
	else
	{ order= 2}

	// show demographics questions at beginning

	var instructions = '<p> You will start by answering some deomgraphic questions </p>';

	instructions += '<div class="ctr"><input type="button" value="Continue" onclick="getDemographics()"/></div>';
	$("#instructions-wrapper").html(instructions);
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
{
	$("#instructions-wrapper").hide(500);
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

	var wrapper = "#displayQ-wrapper_" + iden // There is a different wrapper for each survey type.
	var sent = []; 
	
	
	form2_c= capitalize(form2);

	var sent = new Array();
	sent.push('I feel a bond with ' + form2);
	sent.push('I feel solidarity with ' + form2);
	sent.push('I feel committed to ' + form2);
	sent.push('I am glad to be ' + form1);
	sent.push('I think that ' + form2 + ' have a lot to be proud of');
	sent.push('It is pleasant to be ' + form1);
	sent.push('Being a ' + form1 + ' give me a good feeling');
	sent.push('I often think about the fact that I am a ' + form1);
	sent.push('The fact that I am ' + form1 + ' is an important part of my identity');
	sent.push('Being ' + form1 + ' is an important part of my identity');
	sent.push('I have a lot in common with the average ' + form1);
	sent.push('I am similar to the average ' + form1); // This one is modified slightly
	sent.push(form2_c + ' have a lot in common with each other');
	sent.push(form2_c + ' are very similar to each other');



	for(i=0; i<sent.length; i++)
	{
		likert = createLikert( iden + 'likert_' + i, iden + '_agree_' + i);
	
		// $("divname").css('color','red');

		$(wrapper).append('<div> <li id = "err'+ iden + i + '">' + sent[i]  + '</li> <p>' + likert + '</p></div>')
		//$("#displayQ-wrapper").append('<li>'+ sent[i]  + '</li><p>' + likert + '</p>');
	}

    $(wrapper).shuffle(); 


	$(wrapper).append('<div id="error'+ iden +'" class="error"/>')// appends a unique error id for each section

	//$("#displayQ-wrapper").append('<div id = "error3" class = "error"> </div>'); // put the code for where the error message will go above the button
	

	$(wrapper).append( '<input type="button" value="Continue" onclick = "surveyValidate(\'' + iden +'\')"/>')
	//$("#displayQ-wrapper").append('<div> <input type="button" value="Continue" onclick = "surveyValidate(\'' + iden +'\')"/></div>'); 

	$("#GetPol-wrapper").hide(500); // might have to do some conditionals here with "iden" if the current wrapper is not hiding
	//$("#displayQ-wrapper").show(500);

    

	$(wrapper).show(500);	

}

function surveyValidate(iden)// added iden as an input
{


	var j = 0;
	var error = false; 
	$("li").css('color','black')
	//var errmsg= ''; 


	//var error3= '<div id="error'+ iden +'" class="error"/>'
	
	// $("displayQ").children("div").each(function(index) {
	//	errmsg += '<p> Please provide an answer to question ' + index + '</p>';
	// });

	for(i=0; i <= 13; i++)
	{
		//j += 1; 

		var intermed= iden + '_agree_' + i ; // Used iden to fill in the pre-fix

		qput= 'input[name = ' + intermed + ']:checked';

		Q_input = $(qput).val();

		var wrapper = "#displayQ-wrapper_" + iden





		//Q_input= $('input[name=pol_agree_+i]:checked').val(); 

		if(Q_input == null)
		{
			var errorid = '#err' + iden + i; 
			error = true 
			$(errorid).css('color','#F00'); 

		}

	}


	/*if(error==true)
	{


		$('#error'+ iden).html(errmsg); 


	} */

	if(error==false)
	{   $(wrapper).hide(500); 

		if(iden=="pol")
		{
			if(order==1)
			{
				$("#Nation-wrapper").show(500);
			}
			else
			{
				$("#FreeForm-wrapper").show(500); 
			}

		}
		if(iden=="nat")
		{
			if(order==1)
			{
				$("#FreeForm-wrapper").show(500)
			} 
			else
			{ 
				$("#GetPol-wrapper").show(500)
			}

		}

		if(iden=="free")
		{
			$("#thanks").show(500)
		}



	}

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
		    $("#GetPol-wrapper").show(500);
		}
	    else 
		{
		    $("#Nation-wrapper").show(500);
		}
	} else {   
	order=1;

	    $("#Nation-wrapper").show(500)
	    }
} 




function checkPolitics()
{
	party =$("#affiliation option:selected").val();

	var error = false 
	var errmsg= ""

	if(party == "unselected")
	{ error=true;
		errmsg += "<div class='error'>Please indicate the political party you most identify with</div>";
		$('#error-2').html(errmsg)
	}
	else
	{ 
		if(party=="Democrat")
		{ 
			var pform1="Democrat"
			var pform2="Democrats"
		}

		if(party=="Republican")

		{ 
			var pform1="Republican"
			var pform2="Republicans"
		}
		if(party=="Constitution")
		{ 
			var pform1="Constitution Party member"
			var pform2="Constitution Party members"
		}
		if(party=="Green")
		{ 
			var pform1="Green Party member"
			var pform2="Green Party members"
		}
		if(party=="Libertarian")
		{
			var pform1="Libertarian"
			var pform2="Libertarians"
		}

		$("#GetPol-wrapper").hide(500); 
		displayQ(pform1, pform2, "pol") 
	}


}

function capitalize(string)
{
    return string.charAt(0).toUpperCase() + string.slice(1);
	
}

function CheckNationID()
{ 
    // take list of nations, split into array
    nation_list = $("#national").val().slice(0,-1).split(',');
    nform1 = nation_list.join('-');
    
	n_end = nform1.slice(-1)
	n_ese= nform1.slice(-3)
	//n_ch= nform1.slice(-2)
	
	if(n_end == "s" || n_end == "x" || n_end == "z" || n_end =="h" || n_ese == "ese")
	{
		nform2=nform1
	}
	else 
	{
   
    nform2 = nform1 + "s";
	
	}
	
	
	
	// create array of exceptions to 's' rule
    // check if last nation is exception
    //nform2 = nform1 + "s";
    errmsg=''

	var error = false

	if(nform1.length < 3)
	{ 
		error = true

		errmsg += '<p> Please enter a nationality</p>'

	}
	
	else
	{
		$("#Nation-wrapper").hide(500);
			displayQ(nform1,nform2,"nat");
		
	}// add more to this later
	
	/*

	if(error==true)
	{

		$("#error-4").html(errmsg);

	} else {
	    user_url = $("#user_url").val();
	    $.post("core/validUrl.php", {"user_url":user_url}, function(data) {
		    alert(data);
		    if(data==1) {
			$("#Nation-wrapper").hide(500);
			displayQ(nform1,nform2,"nat");
		    } else {
			$("#error-4").html("Enter a valid URL");
		    }
		});
	}

*/



}

function FreeCheck()
{ 
	nform1 = $("#free1").val()
	nform2 = $("#free2").val()
	errmsg=''
	
	//nform1 = capitalize(nform1) 
	//nform2 = capitalize(nform2)
	
	//nform1 = nform1.charAt(0).toUpperCase() + nform1.slice(1);
	//nform2 = nform2.charAt(0).toUpperCase() + nform1.slice(1); 
	
	


	error = false

	if(nform1.length < 3)
	{ 
		error = true

		errmsg += '<p> Please provide an appropriate answer to item 1 </p>'

		}// add more to this later

		if(nform2.length < 3)
		{ error = true

			errmsg += '<p> Please provide an appropriate answer to item 2 </p>'

		}

		if(error==true)
		{
			$("#error-4").html(errmsg)

		}

		else 
		{
			$("#FreeForm-wrapper").hide(500)
			displayQ(nform1,nform2,"free")
		}

}

function checkDemographics()
{
    gender = $("input[name=gender]:checked").val();
    age = $("#age option:selected").val();
    loc = $("#sel_country option:selected").val();
    races = [];
    $("input[name=race]:checked").each(function() { races.push($(this).val()); });
    income = $("#income").val();
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

    if(gender==null)
	{
	    error=true;
	    errmsg += "<div class='error'>Please choose an option for gender</div>";
	}    
    if(age=="unselected")
	{
	    error=true;
	    errmsg += "<div class='error'>Please state the year you were born</div>";
	}
    if(loc  == "unselected")
	{
	    error=true;
	    errmsg += "<div class='error'>Please indicate your current location</div>";
	}
    if(races.length==0)
	{
	    error=true;
	    errmsg += "<div class='error'>Please indicate your ethnicity</div>";
	}
    if(income==null || $.trim(income) != income.replace(/[^0-9$.,]/g,'') || !IsNumeric(income.replace(/[^0-9.]/g,'')))
	{
	    error=true;
	    errmsg += "<div class='error'>Please enter a valid number for income</div>";
	}
    if(education=="unselected")
	{
	    error=true;
	    errmsg += "<div class='error'>Please indicate your highest level of education</div>";
	}
    // Output error message if input not valid
    if(error==false)
	{

	    $("#demo-wrapper").hide(500);
	    DecideOrder(loc)


		}
    else
	{
	    $('#error-1').html(errmsg);
	}
}

function verify_consent() 
{
    var agree = false;
    var agree2 = false;
    if($("#agree").is(':checked'))
	{ agree = true; }
    if($("#agree2").is(':checked'))
	{ agree2 = true; }
    if(!agree) {
	$("#error_consent").html("Please indicate you have read the information on this page and agree to participate in the study by checking the first box above");
    } else {
	window.location.href = "Authenticate.php?agree=" + (agree ? 1 : 0) + "&agree2=" + (agree2 ? 1 : 0);
    }
        
}
