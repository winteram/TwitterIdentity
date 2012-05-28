$(document).ready(function() {
	
	// add years to age question
	for(i=2000;i>1900;i--)
	{
		$("#age").append('<option value="'+i+'">'+i+'</option>');
	}
	
	
	var order=1;
	
	// show demographics questions at beginning
	
	var instructions = '<p> You will start by answering some deomgraphic questions </p>';
	
	instructions += '<div class="ctr"><input type="button" value="Continue" onclick="getDemographics()"/></div>';
	$("#instructions-wrapper").html(instructions);
	$("#instructions-wrapper").show();
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

function displayPol(form1, form2)
{	

    var i;

    var sent = new Array();
    sent.push('I feel a bond with ' + form2);
    sent.push('I feel solidarity with ' + form2);
    sent.push('I feel committed to ' + form2);
    sent.push('I am glad to be a ' + form1);
    sent.push('I think that ' + form2 + ' have a lot to be proud of');
    sent.push('It is pleasant to be a ' + form1);
    sent.push('Being a ' + form1 + ' give me a good feeling');
    sent.push('I often think about the fact that I am a ' + form1);
    sent.push('The fact that I am ' + form1 + ' is an important part of my identity');
    sent.push('Being ' + form1 + ' is an important part of my identity');
    sent.push('I have a lot in common with the average ' + form1);
    sent.push('I am similar to the average ' + form1); // This one is modified slightly
    sent.push(form2 + ' have a lot in common with each other');
    sent.push(form2 + ' are very similar to each other');

    for(i=0; i<sent.length; i++)
    {
	pol_likert = createLikert("pol_likert_"+i,"pol_agree_"+i);
	$("#displayPol-wrapper").append('<p>'+ sent[i]  + '</p><p>' + pol_likert + '</p>');
    }

    //$("#polquest1").prepend(sents)
    $("#GetPol-wrapper").hide();
    $("#displayPol-wrapper").show(500);
    //$("#polquest1").show(500) 


	
}



// Need to insert other branches this use the "order" variable to determine sequences as wel 
function DecideOrder(location)
{
	if(location == "United States")
	{ 
	    $("#GetPol-wrapper").show(500);
	} else {
	    $("#GetPol-wrapper").show(500);
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
		
		displayPol(pform1, pform2) 
	}
	
	
}

function checkDemographics()
{
    gender = $("input[name=gender]:checked").val();
    age = $("#age option:selected").val();
    loc = $("#loc option:selected").val()
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
    if(races== null)
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
