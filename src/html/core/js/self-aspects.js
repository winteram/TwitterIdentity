// JavaScript Document




var traits_positive = 
	['capable', 'comfortable', 'communicative', 'confident', 'energetic', 
	 'friendly', 'fun and entertaining', 'giving', 'happy', 'hardworking',
	 'independent', 'intelligent', 'interested', 'lovable', 'mature', 'needed', 
	 'optimistic', 'organized', 'outgoing', 'successful'] 

var traits_negative =
	['disagreeing', 'disorganized', 'hopeless', 'immature', 'incompetent', 
	 'indecisive', 'inferior', 'insecure', 'irresponsible', 'irritable', 
	 'isolated', 'lazy', 'like a failure', 'sad and blue', 'self-centered', 
	 'tense', 'uncomfortable', 'unloved', 'weary', 'worthless']


// This is going to have to happen after the buttons are generated. 
// This can be outside the document ready call- which can focus more on display as in the previous thing.

$(document).ready(function() {

	var traits_arr = []

	var self_count = 1 // This defines the self-aspect number

	var trait_dic2={} // This is where someone's self-aspects are stored. Make this a global variable. 

	var edit = false;

	for (var i = 0; i < traits_positive.length; i++) 
	{
    	//$("#trait_buttons").append('<button id = "'+traits_positive[i]+'" style="background-color:transparent" class= "trait_buttons" >'+traits_positive[i]+'</button>')
		button_str =  '<small>';
		button_str +=  '<input id="'+traits_positive[i];
		button_str +=  '" class = "trait_buttons" type="checkbox" checked="unchecked" />';
		button_str +=  ' <label for="'+traits_positive[i]+'">'+traits_positive[i]+'</label>';
		button_str += '</small>'

		$("#trait_buttons").append(button_str);

		$("[id='"+traits_positive[i]+"']").button();

	}
	

 
	$("#trait_buttons").show();

	$('.trait_disp').show()

	$(".trait_buttons").click(function() {	

		if($.inArray(this.id, traits_arr) == -1 ) 
		{
		 
			console.log(traits_arr.push(this.id));

			$('#traits_show').append('<div id= "disp_'+this.id+'" class="t_disp">'+this.id+'</div>');
		
		} 
		else
		{
			var removeItem = $(this).attr("id");

			traits_arr = jQuery.grep(traits_arr, function(value) {
		 		return value != removeItem;
			});

			var j= "[id='disp_"

			var k=$(this).attr("id")

			var l="']"


			toremove=j+k+l;

			$(toremove).remove();
			
	 	}
	
	}); // ends trait_buttons click function

	//console.log(traits_arr)

	$("#add_group").click(function() {   
		console.log(traits_arr)
		
		if(traits_arr.length > 0)
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
				var id_tofill = "#self_display_"+self_count;

				var trait_edit = 'Self-Aspect '+self_count+': '+labelname;
				trait_edit += ' <br> Traits: '+diff_variable;
				trait_edit += ' <br><button  class="edit_button" value="'+self_count+'"> edit </button>';

				$(id_tofill).html(trait_edit);
				
				console.log("conditional in place")
				
				//'Self-Aspect '+self_count+': '+labelname+' <br> Traits Yo: '+diff_variable+'</br><br><button  class="edit_button" value="'+self_count+'"> edit </button>'								
			}
			
			//traits_arr=[]
			console.log(diff_variable);
			$(traits_show).empty();
			
			//$('.trait_buttons').find(':checked').each(function() {
	   		//$(this).removeAttr('checked');
			//$(".trait_buttons").button("refresh")
			//$("#comfortable").click()
			
			var h= self_count.toString();
			var curr_self_aspect= 'self_aspect'+h;
			var traits_curr= 'Traits' + h;
			
	        trait_dic2[curr_self_aspect]=$("#Self-Name").val();
			//console.log(trait_dic2['self_aspect1'])
			trait_dic2[traits_curr]=traits_arr;
			console.log(trait_dic2['Traits1']);
			
			$("#Self-Name").val("");
			
			self_count += 1;
			
			for(var i = 0; i < traits_arr.length; i++) 
			{
				
				$("[id='"+traits_arr[i]+"']").click();	

			}
			
			
		}
		
		// Here is the click function for the edit button

		$(".edit_button").click(function()

		{
			console.log("The click is working");
			
			edit=true;
			
			self_count= $(this).attr("value");
			
			console.log(self_count);
			
			var current_trait='Traits'+self_count;
			
			
			cur_trait_arr=trait_dic2[current_trait]
			
			for(var i = 0; i < cur_trait_arr.length; i++)
			{
				$("[id='"+cur_trait_arr[i]+"']").click();		
			}

		}); // ends the edit button click function
			
		
	}); // ends the add group click function

}); // end the on document ready function






/*


$(document).ready(function(){
	$("#serious").hide()
  $("button").click(function(){
    $("#serious").toggle();
  });
});















*/

