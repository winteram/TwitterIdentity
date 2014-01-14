<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Untitled Document</title>

<script src="core/jquery-ui-1.8.21.custom/js/jquery-1.7.2.min.js" type="text/javascript"></script>
	<script src="core/jquery-ui-1.8.21.custom/js/jquery-ui-1.8.21.custom.min.js" type="text/javascript"></script>
    
   
    <script src="full_self_new.js" type="text/javascript"></script>
    
 
	
	<script src="core/shuffle.js" type="text/javascript"></script>
   <link rel='stylesheet' type='text/css' href='core/self-aspects.css' />
  	<link rel='stylesheet' type='text/css'
	href='core/jquery-ui-1.8.21.custom/css/pepper-grinder/jquery-ui-1.8.21.custom.css' />

    <link href="core_each/css/bootstrap.min.css" rel="stylesheet">

  <link href="core_each/jumbotron-narrow.css" rel="stylesheet">
    
    

</head>

<body bgcolor="#F5F3EF">

  <div class="header"> 
    <span id="idproj-hdr"><img src="core/images/idproj.jpg">
      <img src="core/images/idproj_title.jpg" alt="The Group Identity
      Project"></span>
  </div>



  <div class="section-header" id="section-header-0">Instructions</div>
    <div id="instructions-wrapper" class="wrapper">
      <p> Welcome to the study! To start you will be asked a few demographic questions. You will then be presented a series of questions about what you identify with. The entire survey should take less than 15 minutes and could greatly help us understand how people express their identities in on-line social networks. Thanks in advance for your participation. </p>
      <p> *Note: Though many questions will appear similar to each other, each question has unique features and is important for our analysis. We encourage you to answer them all. </p>  
      
      
     <input type="button" class="ctr" id="fin_intro" value="Continue">


     
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
      <input id="fin_demo" type="button" value="Submit Demographics"/>

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
    <input id="fin_politics" type="button" value="Submit Political Party"/>



   

  </div>


  <div>   
   <ol id="displayQ-wrapper_party" class= "wrapper"></ol>
  </div>





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
    <input id="fin_free" type= reset value="Submit" />
        </p>
        

  </div>





<!-- I'm just putting in this little piece here next to test out a jQuery dialog option-->
<div id= "full-saspect">
<div id="dialog_box" style="display: none;">
    You have information in in the editor window that has not been saved. Editing this Self-Aspect will cause that information to be deleted. Would you like to continue?
</div>

<div id="dialogue_add_group" style="display: none;">
Oops. Looks like there is incomplete information to add a group. You must include a Self-Aspect label name in the textbox and AT LEAST one trait.
</div>


<div id="left_self" class="left-col wrapper">
    <div class="trait_but" id="trait_buttons"> 
    </div>
</div>

<div class="right-col wrapper" id="right_side">

    <form >
    Domain Name: <input type="text" name="GName" id= "Self-Name">
    </form>

    <div class="trait_disp"> 
        Traits 
        <div id ="traits_show"></div>

    </div>
  

  <input type=reset id ="add_group" value= "Add Self-Aspect" />
  


</div>

<div id="finish_SA_but" class="right-col wrapper">

  <p>

  <input type=reset id ="finish_SA" value= "Finish Task" />
</p>

</div>



<div class="wrapper" id="self_labeling">

<div class="panel panel-default">
  <!-- Default panel contents -->
  <div class="panel-heading"><h3>Labeling Self Aspects<h3></div>
  <div class="panel-body">
    <p>Our self-aspects can often be described in terms of different general types. Below is a list of common types of self-aspects with examples. 
     In this next section we would like you to label the self-aspects you generated in the previous section with one of these types listed in the left
     column below, such as 'Situations', 'Roles', etc. If none of the specific types seems to fit, please simply select the "Other" option. </p>
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
</div>






<div id="all_genself">
  <div class="wrapper" id="Self_Q1">
  </div>
  <div class="wrapper" id="Self_Q2">
  </div>

  <div class="wrapper" id="Self_Q3">
  </div>
</div>



<div id="twitterQs" class="wrapper">

   <p> <font size ="5"> What kinds of things do you usually express on Twitter? Please type comments below.</font></p> </br>
       
        <textarea id="tw_express" class= "LargerText" cols="60" rows="5" name="gen_tw_comment"></textarea> </br>

  <div id="PopTwitter">

  </div> 

</div>

<div id = "facebookQs" class="wrapper">

  <p> <font size ="5"> What kinds of things do you usually express on Facebook? Please type comments below.</font></p> </br>
       
        <textarea id="fb_express" class= "LargerText" cols="60" rows="5" name="gen_fb_comment"></textarea> </br>

  <div id="PopFB">
  </div>

</div>









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


<div id="PANAS_scale1" class="wrapper">

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

</body>
</html>