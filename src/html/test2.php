<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Untitled Document</title>

<script src="core/jquery-ui-1.8.21.custom/js/jquery-1.7.2.min.js" type="text/javascript"></script>
	<script src="core/jquery-ui-1.8.21.custom/js/jquery-ui-1.8.21.custom.min.js" type="text/javascript"></script>
    
   
    <script src="self-aspects_2.js" type="text/javascript"></script>
    
 
	
	<script src="core/shuffle.js" type="text/javascript"></script>
   <link rel='stylesheet' type='text/css' href='core/self-aspects.css' />
  	<link rel='stylesheet' type='text/css'
	href='core/jquery-ui-1.8.21.custom/css/pepper-grinder/jquery-ui-1.8.21.custom.css' />

    <link href="core_each/css/bootstrap.min.css" rel="stylesheet">

  <link href="core_each/jumbotron-narrow.css" rel="stylesheet">
    
    

</head>

<body bgcolor="#F5F3EF">


<!-- I'm just putting in this little piece here next to test out a jQuery dialog option-->
<div id= "full-saspect">
<div id="dialog_box" style="display: none;">
    You have information in in the editor window that has not been saved. Editing this Self-Aspect will cause that information to be deleted. Would you like to continue?
</div>

<div id="dialogue_add_group" style="display: none;">
Oops. Looks like there is incomplete information to add a group. You must include a Self-Aspect label name in the textbox and AT LEAST one trait.
</div>


<div class="left-col">
	<div class="trait_but" id="trait_buttons"> 
	</div>
</div>

<div class="right-col" id="right_side">

	<form >
	Domain Name: <input type="text" name="GName" id= "Self-Name">
	</form>

	<div class="trait_disp"> 
		Traits 
		<div id ="traits_show"></div>

	</div>
  

	<input type=reset id ="add_group" value= "Add Self-Aspect" />
  


</div>

<div class="right-col">

  <p>

	<input type=reset id ="finish_SA" value= "Finish Task" />
</p>

</div>

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
