<?php
session_start();
require_once('core/fb-php/src/facebook.php');
require_once('../safe/config.inc');

if (isset($_SESSION['userid']))
{
  $userid = $_SESSION['userid'];
  error_log("IdentitySurvey: ".$userid);
  $agree = isset($_REQUEST['agree']) ? 1 : 0;
  $IUname = isset($_REQUEST['IUName']) ? $_REQUEST['IUName'] : 'none';
  $rqst = $dbh->prepare("UPDATE users SET IUname=:iuname, Agree=:agree WHERE Id=:userid");
  $rqst->bindParam(':iuname',$IUname, PDO::PARAM_STR);
  $rqst->bindParam(':agree',$agree, PDO::PARAM_STR);
  $rqst->bindParam(':userid',$userid, PDO::PARAM_STR);
  $row = $rqst->execute();
}
else 
{
  error_log("ERR: userid not set at IdentitySurvey");
}
?>
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<link rel="shortcut icon" type="image/x-icon" href="core/img/idproj.ico" />
	<title>Aspects of the Self</title>

	<script src="core/jquery-ui-1.8.21.custom/js/jquery-1.7.2.min.js" type="text/javascript"></script>
	<script src="core/jquery-ui-1.8.21.custom/js/jquery-ui-1.8.21.custom.min.js" type="text/javascript"></script>
	<script src="core/js/shuffle.js" type="text/javascript"></script>
	<script src="core/js/trial_newest.js" type="text/javascript"></script>

	<link rel='stylesheet' type='text/css' href='core/css/self-aspects.css' />
	<link rel='stylesheet' type='text/css' href='core/jquery-ui-1.8.21.custom/css/pepper-grinder/jquery-ui-1.8.21.custom.css' />
	<link rel='stylesheet' type='text/css' href="core/css/bootstrap.min.css">
	<link rel='stylesheet' type='text/css' href="core/css/jumbotron-narrow.css">
</head>

<body bgcolor="#F5F3EF">
	<div id="userid" style="display:none"><?php echo $_SESSION['userid']; ?></div>
	<div id="fb_status" style="display:none"><?php echo $_SESSION['fb_status']; ?></div>
	<div id="tw_status" style="display:none"><?php echo $_SESSION['tw_status']; ?></div>

	<div class="header"> 
		<span id="idproj-hdr"><img src="core/img/idproj.jpg">
		<img src="core/img/Aspects_Cover.png" alt="Self-Aspects Study"></span>
	</div>


	<div class ="error" id="error_popup"></div>

	<div class="section-header" id="section-header-0">Instructions</div>

	<div id="instructions" class="wrapper">
		<p> Welcome to the study! To start you will be asked a few demographic questions. 
			You will then be presented a series of questions about aspects of yourself and how you use Facebook and/or Twitter. 
			The entire survey should take less than 50 minutes and could greatly help us understand how people express their 
			identities in on-line social networks. Thanks in advance for your participation. </p>
		<p> *Note: DO NOT attempt to go back to a section by hitting the back button on your browser. Doing this will end the
			survey.</p>  
		<input type=reset class="ctr" id="fin_intro" value="Continue" />			
	</div>

	
	<div class="section-header" id="section-header-1">About you</div>
	<div id="demo-wrapper" class="wrapper">
		<form id="demographics">
			<ol>
				<li id ="genderq"><p>Gender</p>
					<p> 
						<input id="gender_male" name="gender" type="radio" value="M"/>
						<label for="gender_male">Male</label>
						<br>     
						<input id="gender_female" name="gender" type="radio" value="F"/>
						<label for="gender_female">Female</label>
						<br>     
						<input id="gender_none" name="gender" type="radio" value="decline"/>
						<label for="gender_none">Decline to answer</label>
					</p>
				</li>         
				<li id = "ageq"><p><label for="age">Year of Birth</label></p>
					<p> 
						<select id="age" name="age">
							<option value="unselected" selected="selected"></option>
						</select>
					</p> 
				</li>         
						 
				<li id = "ethnicityq">
					<p>Ethnicity. Check all that apply</p>
					<p>      
						<input id="race_white" name="race" type="checkbox" value="white"/> 
						<label for="race_white">White</label>
						<br>      
						<input id="race_black" name="race" type="checkbox" value="black"/> 
						<label for="race_black">Black, African-American</label>
						<br>    
						<input id="race_latino" name="race" type="checkbox" value="latino"/> 
						<label for="race_latino">Hispanic or Latino</label>
						<br>
						<input id="race_indian" name="race" type="checkbox" value="indian"/> 
						<label for="race_indian">Asian Indian</label>
						<br> 
						<input id="race_asian" name="race" type="checkbox" value="asian"/> 
						<label for="race_asian">Other Asian</label>
						<br>
						<input id="race_hawaii" name="race" type="checkbox" value="hawaiian"/> 
						<label for="race_hawaii">Hawaiian, Pacific Islander</label>
						<br> 
						<input id="race_amind" name="race" type="checkbox" value="amind"/> 
						<label for="race_amind">American Indian or Alaskan Native</label>
						<br> 
						<input id="race_other" name="race" type="checkbox" value="other"/> 
						<label for="race_other">Other</label>
					</p>			
				</li> 

				<li id ="incomeq">
					<p> 
						<label for="income" >Annual Income (in US dollars; click <a href="http://finance.yahoo.com/currency-converter/?u#from=GBP;to=USD;amt=1" target="_blank">here</a> for currency conversion)</label>        
					</p> 
					<p>
						<select id = "income" name ="income">
						<option value="unselected" selected="selected"></option>
						<option value = "1">0-$20,000</option>
						<option value = "2">$20,000-$40,000</option>
						<option value = "3">$40,000-$60,000</option>
						<option value = "4">$60,000-$80,000</option>
						<option value = "5">$80,000-$100,000</option>
						<option value = "6">$100,000-$200,000</option>
						<option value = "7">More than $200,000</option>
						<option value = "8">Would rather not say</option>
						</select>
					</p> 
				</li>         

				<li id ="educationq">
					<p> 
						<label for="edu">Highest education level attained</label>        
					</p> 
					<p>
						<select id="edu" name="edu"> 
							<option value="unselected" selected="selected"></option>
							<option value="none">No schooling completed, or less than 1 year</option>
							<option value="elem">Nursery, kindergarten, and elementary (grades 1-8)</option>
							<option value="hs">High school (grades 9-12, no degree)</option>
							<option value="hsgrad">High school graduate (or equivalent)</option>
							<option value="college">Some college (1-4 years, no degree)</option>
							<option value="as">Associate's degree (including occupational or academic degrees)</option>
							<option value="bs">Bachelor's degree (BA, BS, AB, etc)</option>
							<option value="ms">Master's degree (MA, MS, MENG, MSW, etc)</option>
							<option value="md">Professional school degree (MD, DDC, JD, etc)</option>
							<option value="phd">Doctorate degree (PhD, EdD, etc)</option>
						</select>
					</p> 
				</li>
			</ol>
			<input id="fin_demo" type="button" value="Submit Demographics" onclick="checkDemographics();"/>

		</form>
	</div>

	<div class="section-header" id="politics_h">Politics</div>
	<div id="GetPol-wrapper" class="wrapper">

		<p> Generally speaking, do you usually think of yourself as a Republican, a Democrat, an Indendepent, or what?
			Please select the group with which you most identify. 

		</p>

		<label for = "party"> Party </label>
		<select id ="affiliation" name= "party">
			<option value= "unselected" selected= "selected"></option>
			<option value= "democrat"> Democratic Party </option>
			<option value = "republican"> Republican Party </option>
			<option value = "independent"> Independent </option>
			<option value = "green"> Green Party </option>
			<option value = "libertarian"> Libertarian Party </option>
			<option value = "green"> Green Party </option>
			<option value = "constitution"> Constitution Party </option>
		</select>

		<p> Add Comment <textarea id="party_com"cols="50" rows="1" name="party_com"></textarea></p>
				
		<p>How would you describe your political views?</p>

		<table class="likert" id="pol_spectrum" >
			<tr>

				<td><input type="radio" name="pol_spec" value="1" /></td>
				<td><input type="radio" name="pol_spec" value="2" /></td>
				<td><input type="radio" name="pol_spec" value="3" /></td>
				<td><input type="radio" name="pol_spec" value="4" /></td>
				<td><input type="radio" name="pol_spec" value="5" /></td>
				<td><input type="radio" name="pol_spec" value="6" /></td>
				<td><input type="radio" name="pol_spec" value="7" /></td>
			</tr>

			<tr>
				<td>Strongly Conservative</td> 
				<td></td>
				<td></td>
				<td>Moderate</td>
				<td></td>
				<td></td>
				<td>Strongly Liberal</td>
			</tr>
		</table>
		<div id="error-2"></div>
		<input id="fin_politics" type="button" value="Submit Political Party" onclick="checkPolitics();"/>

	</div>


	<ol id="displayQ-wrapper_party" class= "wrapper"></ol>


	<div class="section-header" id="free_h"> Free Response Identity</div>
	<div id="FreeForm-wrapper" class="wrapper">

		<p>We all have groups we identify with.For this part, we would like you to think about groups you feel committed to, one's 
			at form an important part of your identity. You will be asked three questions about EACH identity. For each subsection, like 
			"Identity 1", all three questions are asking about the SAME identity. So for instance, if the identity you were thinking of was 
			your political identity, your answers might be "Democrat", "Democrats" and "democrats.org"  </p>
		<h3> Idenitity 1</h3>
		<ol>
			<li id = "freeq11"> I see myself as a <input id="free11" name="freeform11" type="text"/> <span><i> e.g. Democrat </i> </span></li> 
			<br />
			<li id = "freeq12"> I identify with other <input id ="free12" name = "freeform12" type="text"/> <span><i> e.g. Democrats</i> </span> </li> 
		
			<li id = "freeq13">
				<p> In the box below, please put a website that relates to this identity </p> 
				
				<input id ="user_url1" name = "user_url1" type="text"/> <span><i> e.g. democrats.org </i> </span>
			</li> 
		</ol>
		<h3> Identity 2 </h3>
		<ol>
			<li id = "freeq21"> I see myself as a <input id="free21" name="freeform21" type="text"/> </li>
			<br />
			<li id = "freeq22"> I identify with other <input id ="free22" name = "freeform22" type="text"/> </li>
		
			<li id = "freeq23">
				<p> In the box below, please put a website that relates to this identity </p> 
				<input id ="user_url2" name = "user_url2" type="text"/>
				<!-- Moved the above input inside the list item -->
			</li> 
		</ol>
				
		<h3> Identity 3</h3>
		<ol>
			<li id = "freeq31"> I see myself as a <input id="free31" name="freeform31" type="text"/> </li>
			<br />
			<li id = "freeq32"> I identify with other <input id ="free32" name = "freeform32" type="text"/> </li>
		
			<li id = "freeq33">
				<p> In the box below, please put a website that relates to this identity </p>
				<input id ="user_url3" name = "user_url3" type="text"/>
				<!-- Moved the above input inside the list item -->
			</li>
		</ol>
					
		<p>
			<div id="error-5" class="error"></div>       
			<input id="fin_free" type= reset value="Submit" onclick="FreeCheck();" />
		</p>
	</div>




	<!-- I'm just putting in this little piece here next to test out a jQuery dialog option-->

	<div class="section-header" id="self-aspect_h">Self-Aspects</div>
	<div id= "full-saspect" class="wrapper">
		<div id= "self_task_instructions" title="Self Aspects Instructions">
			<p>
				In this task, you will be asked to describe aspects of your personal life. It is important that you read ALL instructions so that you’ll know what to do at all times. 
				You can return to these instructions at any time by pressing the "View Instructions" button that will appear on the screen when
				this window is closed.
			</p>

			<p>
				We are interested in how you describe yourself.  You will be presented with a series of terms 
				in a list on the left side of a window, which are clickable buttons.  Each term is the name of a trait or 
				characteristic.  Your task is to form groups of traits that go together, where each group of traits describes an aspect of you
				or your life.  You may sort the traits into groups on any meaningful basis – but remember to think about yourself while doing 
				this. Each group of traits might represent a different aspect of yourself.  Form as many or as few groups as you desire. 
				Continue forming groups until you feel that you have formed the important ones.  We realize that this task could be endless, 
				but we want only what you feel is meaningful to you.  When you feel that you are straining to form more groups, it is probably a 
				good time to stop.
			</p>

			<p>
				In order to form a group, you’ll use the mouse to click on traits in the left-hand column.
				When you click on the traits, they will ‘bounce’ to the right-hand window.  If you wish to remove one or more of these traits, press
				the trait button again (it will bounce back to the left side). 
			</p>

			<p>
				Each group may contain as few or as many traits as you wish.  You do not have to use every trait, only those that you feel are 
				descriptive of you.  Also, each trait may be used in more than one group; so you may keep reusing traits as many times as you 
				like.  For example, you may find that you want to use the trait ‘relaxed’ in several groups.
			</p>

			<p>
				Once you have the traits you want listed on the right hand side, you should label what this collection of traits means to you.  
				In other words, what is it about yourself that you are describing?  Type your description in the text box located on the right
				side of the screen labeled- "Self-Aspect Name".  Once you’ve selected the traits and named the group, 
				press the "Add Self Aspect" button to record it. Once you record a group, you can edit it later, by hitting the edit button located
				in a box with that group. Note: you cannot edit a previously recorded group if you are currently creating another group. 
				The current trait window and Self-Aspect Name box must be empty to edit a group you've previously recorded.	
			</p>
		</div>

		<div id="dialog_box" style="display: none;">
			You have information in in the editor window that has not been saved. 
			Editing this Self-Aspect will cause that information to be deleted. 
			If you wish to edit a new self-aspect, add the one you are currently editing.
		</div>

		<div id="dialogue_add_group" style="display: none;">
			Oops. Looks like there is incomplete information to add a group. 
			You must include a Self-Aspect label name in the textbox and AT LEAST one trait.
		</div>

		<div class="left-col">
		
		</br>
		<p>
			<input class='btn btn-warning' type=button id ="aspect_instruct_button" value= " View Instructions" />
		</p>
		<h3> Trait Buttons </h3>
		<p class="trait_info"> 
			Click the trait buttons below to include them in a Self-Aspect in the
			column to the right entitled, "Current Self-Aspect". To remove a trait
			that has been added, simply press the trait button again.
		</p>
		<div class="trait_but" id="trait_buttons"> </div>
		</div>

		<div class="outer-right-col">
			<div class="center-col">
			
			<h3> Current Self-Aspect </h3>

				<!-- removed the form here, changed to p and span -->
				<p>
					<span><b>Self-Aspect Name: </b></span>
					<input type="text" name="GName" id= "Self-Name">
				</p>

				<div class="trait_disp"> 
					<h4>Traits</h4> 
					<div id ="traits_show"></div>
				</div>
			
				<input class='submit-button' type=button id ="add_group" value= "Add Self-Aspect" onclick="add_group_click();"/>

				<!-- Included the next bit into a single section with class right-col -->
			</br>
			</br>
				
			</div>
			<div class="right-col" id="right_side">
				<p class="finish_aspects_button">
					<input class="btn btn-success btn-large" type=button id ="finish_SA" value= "Finish Task" onclick="finish_SA_click();"/>
				</p>
			</div>
		</div>

	</div>
	<div style='clear:both;' />


	<div class="wrapper" id="self_labeling">

		<div class="panel panel-default">
			<!-- Default panel contents -->
			<div class="panel-heading"><h3>Labeling Self Aspects<h3></div>
			<div class="panel-body">
				<p>Our self-aspects can often be described in terms of different general types. Below is a list of common types of self-aspects with examples. 
				 In this next section we would like you to label the self-aspects you generated in the previous section with one of these types listed in the left
				 column below, such as 'Situations', 'Roles', etc. If none of the specific types seems to fit, please simply select the "Other" option. When you
				 are all done, press the Finish Task button to continue to the next section. </p>
			</div>

			<!-- Table -->
			<table class="table" table border=1>
				<tr>
					<td><h4><b>Type</b><h4></td>
					<td><b><h4><b>Examples</b><h4></b></td>
					
				</tr>
				<tr>
					<td> Situations</td>
					<td> When in a crowded situation, when meeting new people</td>
				</tr>

				<tr>
					<td>Relationship</td>
					<td>With my boyfriend, with my family</td>
				</tr>

				<tr>
					<td>Roles</td>
					<td>Daughter, as a student</td>
				</tr>
				<tr>
					<td>Emotional</td>
					<td>When I'm freaking out, my positive qualities</td>
				</tr>
				<tr>
					<td>True Selves</td>
					<td>The real me, who I really am</td>
				</tr>
				<tr>
					<td>Goals</td>
					<td>Who I ought to be, who I'm afraid I will be</td>
				</tr>
				<tr>
					<td>Time Related</td>
					<td>The old me, my future me</td>
				</tr>
				<tr>
					<td>Public</td>
					<td>How others see me, the public me</td>
				</tr>
				<tr>
					<td>Alone</td>
					<td>When I'm alone, by myself</td>
				</tr>
				<tr>
					<td>Other</td>
					<td></td>
				</tr>
			</table>
		</div>
		<form id="self_labeling_form"></form>
	</div>






	<div class="section-header" id="self-aspect_h">Self Questionnaire</div>
	<div id="all_genself">
		<div class="wrapper" id="Self_Q1">
		</div>
		<div class="wrapper" id="Self_Q2">
		</div>
		<div class="wrapper" id="Self_Q3">
		</div>
	</div>



	<div class="section-header" id="self-aspect_h">Social Media Questions</div>
	<div id="twitterQs" class="wrapper">
		<h3> Twitter Usage </h3>

		<p> What kinds of things do you usually express on Twitter? Please type comments below.</p> </br>
				 
		<textarea id="tw_express" class= "LargerText" cols="60" rows="5" name="gen_tw_comment"></textarea> </br>

		<div id="PopTwitter"></div> 

	</div>

	<div id = "facebookQs" class="wrapper">
	 	<h3> Facebook Usage </h3>

		<p> What kinds of things do you usually express on Facebook? Please type comments below </p> </br>
		
		<textarea id="fb_express" class= "LargerText" cols="60" rows="5" name="gen_fb_comment"></textarea> </br>

		<div id="PopFB"></div>

	</div>








	<div class="section-header" id="self-aspect_h">Introspection Questionnaire</div>

	<div id="contingencies2" class="wrapper">



			<table class="likert" table border=1 id="con_table2">
				<tr class="likert2">
					<td style="width:320px"></td>
					<td>Strongly Disagree</td>
					<td>Disagree</td>
					<td>Disagree Somewhat</td>
					<td>Neutral</td>
					<td>Agree Somewhat</td>
					<td>Agree</td>
					<td>Strongly Agree</td>
				</tr>
			
			</table>

	</div>



	<div id="contingencies1" class="wrapper">
			<div id="cont_instruct">
			INSTRUCTIONS: Please respond to each of the following statements, on this and the next two pages, by circling your answer using 
			the scale from "1 = Strongly disagree" to "7 = Strongly agree.”  If you haven't experienced the situation described in a 
			particular statement, please answer how you think you would feel if that situation occurred.  

			<p> <h4>Page 1 of 3</h4> </p>
		</div>

			<table class="likert" table border=1 id="con_table1">
				<tr class="likert2">
					<td style="width:320px"></td>
					<td>Strongly Disagree</td>
					<td>Disagree</td>
					<td>Disagree Somewhat</td>
					<td>Neutral</td>
					<td>Agree Somewhat</td>
					<td>Agree</td>
					<td>Strongly Agree</td>
				</tr>
			
			</table>

	</div>



	<div id="contingencies3" class="wrapper">


			<table class="likert" table border=1 id="con_table3">
				<tr class="likert2">
					<td style="width:320px"></td>
					<td>Strongly Disagree</td>
					<td>Disagree</td>
					<td>Disagree Somewhat</td>
					<td>Neutral</td>
					<td>Agree Somewhat</td>
					<td>Agree</td>
					<td>Strongly Agree</td>
				</tr>
			
			</table>

	</div>


	<div class="section-header" id="self-aspect_h">Affective Questionnaire</div>
	<div id="PANAS_scale1" class="wrapper">

		<div id="PANAS_instruct">

			<p>
				You will now complete some questions about how you feel in general.  Please be as honest as possible.  
				Remember, there is no right or wrong answer; answer in a way that is right for you.  Your answers will remain confidential.


			</p>

			<h3> Mood: Positive and Negative Affect Schedule </h3>

				<p>
					This scale consists of a number of words that describe different feelings and emotions. Read each item and then
					 mark the appropriate answer in the space next to that word. Indicate to what extent <b>you feel this way in general</b>. 
					 Use the following scale to record your answers.
				</p>


		</div>

		<table class="likert" table border=1 id="PANAS_table1">
			<tr class="likert2">
				<td style="width:40px"></td>
				<td>Very Slightly or Not at All</td>
				<td>A Little</td>
				<td>Moderately</td>
				<td>Quite a Bit</td>
				<td>Extremely</td>
			</tr>

		</table>

	</div>


	<div id="PANAS_scale2" class="wrapper">
		 <h3> Mood: Positive and Negative Affect Schedule </h3>


			<table class="likert" table border=1 id="PANAS_table2">
				<tr class="likert2">
					<td style="width:40px"></td>
					<td>Very Slightly or Not at All</td>
					<td>A Little</td>
					<td>Moderately</td>
					<td>Quite a Bit</td>
					<td>Extremely</td>
				</tr>

			</table>

	</div>

	<div class="section-header" id="feedback_h">Feedback</div>
		<div id="GetFeedback-wrapper" class="wrapper"> </br>
			<div style='margin:auto; width: 80%; font-size:1.5em'> 
				We value any feedback you would like to give us on this study. Please type comments below.
			</div> 
			<div style='margin:0 auto; width: 50%;'> 
				<textarea id="feedback" class= "LargerText" cols="80" rows="8" name="comment"></textarea> 
			</div>
			<div style='margin:0 auto; width: 50%;'> 
				<input style='margin:10px 40%;' class="submit-button" id="fin_feedback" type=button value="Submit Feedback"/>
			</div>
		</div>


		<div id="thanks" class="wrapper">
			<h2 class= "center-title1"> THANKS FOR YOUR SUPPORT!</h2>
			</br>
			</br>
			<div align="center">
				<h4> If you are an IU student, your experimental credit will be posted within the next 48 hours.
				 Please share us on Facebook and/or Twitter by clicking the buttons below.
				</h4>

				</br>

				<a href="http://www.facebook.com/share.php?u=http://www.smallsocialsystems.com/groupid"><img src="core/img/facebook-share-button.png"></a>

				</br>
				</br>
				<a href="http://twitter.com/home?status= I just helped science by participating in a Psychology study: http://www.smallsocialsystems.com/groupid"><img src="core/img/twitter-share-button.png"></a>

			</div>

		</div>
	</div>



</body>
</html>