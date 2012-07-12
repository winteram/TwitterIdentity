<?php 
session_start();
require_once('core/locations.php');
require_once('../safe/config.inc');
?>

<html>
<head>
	<title>Group Identity Project</title>
	<script src="core/jquery-ui-1.8.21.custom/js/jquery-1.7.2.min.js" type="text/javascript"></script>
	<script src="core/jquery-ui-1.8.21.custom/js/jquery-ui-1.8.21.custom.min.js" type="text/javascript"></script>
	<script src="core/IdentitySurvey.js" type="text/javascript"></script>
	<script src="core/shuffle.js" type="text/javascript"></script>
	<script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src="//platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");</script>
	<link rel="shortcut icon" href="core/images/idproj.ico" type="image/x-icon" />
	<link rel='stylesheet' type='text/css'
	href='core/jquery-ui-1.8.21.custom/css/pepper-grinder/jquery-ui-1.8.21.custom.css' />
	<link rel='stylesheet' type='text/css' href='core/IdentitySurvey.css' />
</head>
<body>

	<div class="header"> 
		<span id="idproj-hdr"><img src="core/images/idproj.jpg">
			<img src="core/images/idproj_title.jpg" alt="The Group Identity
			Project"></span>
		</div>

		<div id="twitid" style="display:none"><?php echo $_SESSION['twitid']; ?></div>
		<div class="section-header" id="section-header-0">Instructions</div>
		<div id="instructions-wrapper" class="wrapper">
			<p> Welcome to the study! To start you will be asked a few demographic questions. You will then be presented a series of questions about what you identify with. The entire survey should take less than 15 minutes and could greatly help us understand how people express their identities in on-line social networks. Thanks in advance for your participation. </p>
            <p> *Note: Though many questions will appear similar to each other, each question has unique features and is important for our analysis. We encourage you to answer them all. </p>
            
            
			<div class="ctr"><input type="button" value="Continue" onClick="getDemographics()"/></div>
		</div>

		<div class="section-header" id="demographics_h">Demographics</div>
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
						<span> 
							<select id="age" name="age">
								<option value="unselected" selected="selected"></option>
							</select>
						</span> 
					</li>         
					<li id = "locationq">
						<p> 
							<label for="loc">Location</label>        
						</p> 
						<p> 
                            
							<select name="country" id= "sel_country">
                            <option value="unselected" selected="selected"></option>
								<?php foreach($Countries as $abbr => $country)
							echo "<option value=" . $abbr . ">" . $country . "</option>"; 
							?>
						</select>
					</p> 

				</li>  
				       
				<li id = "ethnicityq">
					<p>Ethnicity. Check all that apply</p>
                </li> 
					<p>      
						<input id="race_white" name="race" type="checkbox" value="white"/> 
						<label for="race_white">White</label>
						<br>      
						<input id="race_black" name="race" type="checkbox" value="black"/> 
						<label for="race_black">Black, African-American, or Negro</label>
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
			<div class ="error" id="error-1"></div>
			<input type="button" value="Submit Demographics" onClick="checkDemographics()"/>
		</form>

	</div>


	<div class="section-header" id="politics_h">Politics</div>
	<div id="GetPol-wrapper" class="wrapper">

		<p> Of these political parties, which do you most identify with?</p>

		<label for = "party"> Party </label>
		<select id ="affiliation" name= "party">
			<option value= "unselected" selected= "selected"></option>
			<option value= "democrat"> Democratic Party </option>
			<option value = "republican"> Republican Party </option>
			<option value = "constitution"> Constitution Party </option>
			<option value = "green"> Green Party </option>
			<option value = "libertarian"> Libertarian Party </option>
		</select>
        <p/>
		<div id="error-2"></div>
		<input type="button" value="Submit Political Party" onClick="checkPolitics()"/>

	</div>

	<div class="section-header" id="nationality_h"> Nationality</div>
	<ol id="Nation-wrapper" class="wrapper">

		<p> In this section you will be indicating which nationality or
			nationalities you identify with. In the text box below you will start to
			type your nationality. As you type, options will appear in a drop down
			menu below the text box. If you are a US citezen, type "American". 
		</p> 

		<p> <b>*Important:</b> for our system to register your choice, you must
			<b>CLICK</b> on the drop down item corresponding with your
			nationality/nationalities. When you select a nationality from the menu, a
			comma (",") will be inserted after it. If you identify with more than one
			nationality, simply begin typing each additional nationality after the
			ones you have previously listed. Again, as you type options will appear in
			the drop menu, please click the one corresponding to the nationality you
			identify with. 
		</p> 

		<div id="nationalityq" class="ui-widget"> I see myself as <input id="national" name="nationality" size="50"/></div> 
		<div id="error-4" class="error"> </div>

		<p><input type="button" value="Submit" onClick= "CheckNationID()"/></p>

	</ol>

	<div class="section-header" id="free_h"> Free Response Identity</div>
	<div id="FreeForm-wrapper" class="wrapper">

		<p>We all have groups we identify with. In a given moment we may see ourselves as Democrats, or Americans, Germans, Fathers, Mac People, Women, Teachers, Soccer Players, etc. For this part, we would like you to think about groups you feel committed to, one's that form an important part of your identity. You will be asked three questions about EACH identity. For each subsection, like "Identity 1", all three questions are asking about the SAME identity. </p>
        <h3> Idenitity 1</h3>
        <ol>
		<li id = "freeq1"> I see myself as a <input id="free1" name="freeform1" type="text"/> <span><i> e.g. Democrat </i> </span></li> 
		<br />
		<li id = "freeq2"> I identify with other <input id ="free2" name = "freeform2" type="text"/> <span><i> e.g. Democrats</i> </span> </li> 
		
		<li id = "freeq3">
        <p> In the box below, please put a website that relates to this identity </p> 
        
        <input id ="user_url" name = "user_url" type="text"/> <span><i> e.g. democrats.org </i> </span></li> 
       </ol>
        <h3> Identity 2 </h3>
        <ol>
        <li id = "freeq4"> I see myself as a <input id="free3" name="freeform3" type="text"/> </li>
		<br />
		<li id = "freeq5"> I identify with other <input id ="free4" name = "freeform4" type="text"/> </li>
		
		<li id = "freeq6">
        <p> In the box below, please put a website that relates to this identity </p> </li>
        
        <input id ="user_url2" name = "user_url2" type="text"/>
        </ol>
        
        
          <h3> Identity 3</h3>
          <ol>
        <li id = "freeq7"> I see myself as a <input id="free5" name="freeform5" type="text"/> </li>
		<br />
		<li id = "freeq8"> I identify with other <input id ="free6" name = "freeform6" type="text"/> </li>
		
		<li id = "freeq9">
        <p> In the box below, please put a website that relates to this identity </p> </li>
        
        <input id ="user_url3" name = "user_url2" type="text"/>
        </ol>
       
        
        <p>
		<div id="error-5" class="error"></div>       
		<input type="button" value="Submit" onClick= "FreeCheck()"/>
        </p>
        

	</div>
    
    <div class="section-header" id="feedback_h">Feedback</div>
	<div id="GetFeedback-wrapper" class="wrapper"> </br>

		<center> <p> <font size ="5"> We value any feedback you would like to give us on this study. Please type comments below.</font></p> </center> </br> </br>
       
        <center><textarea id="feedback" class= "LargerText" cols="60" rows="20" name="comment"></textarea> </br></center>
       


		
		<center><input type="button" value="Submit Feedback" onClick="Thanks()"/></center>

	</div>



	<ol id="displayQ-wrapper_party" class= "wrapper"></ol>

	<ol id="displayQ-wrapper_nation" class= "wrapper"></ol>

	<ol id="displayQ-wrapper_own" class= "wrapper"></ol>

	<div id="thanks" class="wrapper">
		<h2 class= "center-title1"> THANKS FOR YOUR SUPPORT!</h2>
		<div class="container">
			<div class="center-section">
			<div class="center-para">
				You have finished the survey portion of the study. We appreciate you taking the time to participate. This research would not be possible without your help. 
<?php
			if($_SESSION['agree2'] == 1)
				echo "<p>To participate in the experimental portion of the study, <u>remember to follow us on Twitter by clicking the link below.</u><br><br>";
			else
				echo "<p><u>We encourage you to follow us on Twitter</u><br><br>";
?>
				<a href="https://twitter.com/GroupID_Project" class="twitter-follow-button" data-show-count="false" data-lang="en" data-size="large">Follow @GroupIdentity</a></p>

<!--
       You have been entered into the drawing. So that we can direct message you if you win, however, it is not necessary to follow us to be in the drawing. Should you win, we can always mention you and you can respond to our mention with the address to send the prize to. */

<p>If you agreed to participate in the experimental portion of the
study, we will be in contact on Twitter. If you would like to
participate in the experiment and did not indicate this on the
initial consent form, you may participate by clicking on the
following link:</p>
-->    

				<h3 class="center-title"> HELP SPREAD THE WORD</h3>
				<span> We hope you share this study with your followers on Twitter!  Click the "Tweet" button to share!</span>
				<span style="margin-left:10px;"><a href="https://twitter.com/share" class="twitter-share-button"
					data-lang="en" data-count="none" data-size="large" 
					data-url='http://smallsocialsystems.com/asaf/AboutUs.html?flag=<?php echo encode_salt($_SESSION["twitid"]);?>+'
					data-text='I just participated in the Group Identity Project! Check it out: '>Tweet</a></span>

				<p> Thanks again, </br></br> Winter and Asaf. </p>
			</div>
			</div>
			<div class="footer">
				<div id="contact-info">
					For more information, contact:<br>
					Group Identity Project<br>
					group.id.project [at] gmail.com<br>
				</div>
			</div>
		</div>
	</div>

	<div id="tester" class="wrapper"></div>

