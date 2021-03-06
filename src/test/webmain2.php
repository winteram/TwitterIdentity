<html>
<head>
<?php require_once "locations.php"; ?>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.5.2/jquery.min.js" type="text/javascript"></script>
<!-- <script src="jquery.min.js" type="text/javascript"></script> -->
<script src="WebSurvey2.js" type="text/javascript"></script>
<link rel='stylesheet' type='text/css' href='WebSurvey.css' />
</head>
<body>

<div class="header" id="header-0">Instructions</div>
<div id="instructions-wrapper" class="wrapper">
  <div id="base-instructions" class="instructions">
  </div>
</div>
	
<div class="header" id="header-1">About you</div>
<div id="demo-wrapper" class="wrapper">
    <form id="demographics">
        <ol>
            <li><p>Gender</p>
                <p> 
                    <input id="gender_male" name="gender" type="radio" value="Male"/>
                    <label for="gender_male">Male</label>
                <br>     
                    <input id="gender_female" name="gender" type="radio" value="Female"/>
                    <label for="gender_female">Female</label>
                <br>     
                    <input id="gender_none" name="gender" type="radio" value="none"/>
                    <label for="gender_none">Decline to answer</label>
                </p>
            </li>            
            <li><p><label for="age">Year of Birth</label></p>
                <span> 
                    <select id="age" name="age">
                        <option value="unselected" selected="selected"></option>
	 				</select>
                </span> 
            </li>         
            <li>
              <p> 
                <label for="loc">Location</label>        
              </p> 
              <p> 
		<select name="country">
		  <?php foreach($Countries as $abbr => $country)
		  echo "<option value=" . $abbr . ">" . $country . "</option>"; 
		  ?>
		</select>
              </p> 
              
            </li>         
            <li>
                <p>Ethnicity</p>
                <p>      
                    <input id="race_white" name="race" type="checkbox" value="White"/> 
                    <label for="race_white">White</label>
                <br>      
                    <input id="race_black" name="race" type="checkbox" value="Black"/> 
                    <label for="race_black">Black, African-American, or Negro</label>
                <br>    
                    <input id="race_latino" name="race" type="checkbox" value="Latino"/> 
                    <label for="race_latino">Hispanic or Latino</label>
                <br>
                    <input id="race_indian" name="race" type="checkbox" value="Indian"/> 
                    <label for="race_indian">Asian Indian</label>
                <br> 
                    <input id="race_asian" name="race" type="checkbox" value="Asian"/> 
                    <label for="race_asian">Other Asian</label>
                <br>
                    <input id="race_hawaii" name="race" type="checkbox" value="Hawaiian"/> 
                    <label for="race_hawaii">Hawaiian, Pacific Islander</label>
                <br> 
                    <input id="race_amind" name="race" type="checkbox" value="AmInd"/> 
                    <label for="race_amind">American Indian or Alaskan Native</label>
                <br> 
                    <input id="race_other" name="race" type="checkbox" value="Other"/> 
                    <label for="race_other">Other</label>
                </p>
            </li>         
            <li>
                <p> 
                    <label for="income">Annual Income (in US dollars; click <a href="http://finance.yahoo.com/currency-converter/?u#from=GBP;to=USD;amt=1" target="_blank">here</a> for currency conversion)</label>        
                </p> 
                <p>
                    <input id="income" name="income" type="text"/> 
                </p> 
            </li>         
            <li>
                <p> 
                    <label for="edu">Highest education level attained</label>        
                </p> 
                <p>
                    <select id="edu" name="edu"> 
                        <option value="unselected" selected="selected"></option>
                        <option value="none">No schooling completed, or less than 1 year</option>
                        <option value="elem">Nursery, kindergarten, and elementary (grades 1-8)</option>
                        <option value="high">High school (grades 9-12, no degree)</option>
                        <option value="hs">High school graduate (or equivalent)</option>
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
		<div id="error-1"></div>
        <input type="button" value="Submit Demographics" onClick="checkDemographics()"/>
    </form>
    
</div>







<div id="GetPol-wrapper" class="wrapper">

  <p> Which US political party do you most identify with?</p>
 

  <label for = "party"> Party </label>
  <select id ="affiliation" name= "party">
    <option value= "unselected" selected= "selected"></option>
    <option value= "Democrat"> Democratic Party </option>
    <option value = "Republican"> Republican Party </option>
    <option value = "Constitution"> Constitution Party </option>
    <option value = "Green"> Green Party </option>
    <option value = "Libertarian"> Libertarian Party </option>
  </select>
 
  <div id="error-2"></div>
  <input type="button" value="Submit Demographics" onClick="checkPolitics()"/>
 

 
</div>
 
<ol id="displayQ-wrapper" class= "wrapper">

</ol>