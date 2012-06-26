<?php 
session_start();
?>
<html>
<head>
<title>Group Identity Project</title>
<script src="core/jquery-ui-1.8.21.custom/js/jquery-1.7.2.min.js" type="text/javascript"></script>
<script src="core/jquery-ui-1.8.21.custom/js/jquery-ui-1.8.21.custom.min.js" type="text/javascript"></script>
<script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src="//platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");</script>
<script type="text/javascript"> $("button").button(); </script>
<link rel='stylesheet' type='text/css'
      href='core/jquery-ui-1.8.21.custom/css/pepper-grinder/jquery-ui-1.8.21.custom.css' />
<link rel='stylesheet' type='text/css' href='core/IdentitySurvey.css' />
</head>
<body bgcolor="#F5F3EF">

<div class="header"> 
  <span id="idproj-hdr"><img src="core/images/idproj.jpg">
  <img src="core/images/idproj_title.jpg" alt="The Group Identity
  Project"></span>
</div>

<h2 class= "center-title1"> THANKS FOR YOUR SUPPORT!</h2>

<div class="container">
  
    <div class="center-section">
      <div class="center-para">You have finished the survey portion of
      the study. We appreciate you taking the time to participate. This
      research would not be possible without your help. 

<?php
if($_SESSION['agree2'] == 1)
  echo "<p>To participate in the experimental portion of the study, <u>remember to follow us on Twitter by clicking the link below.</u><br><br>";
else
  echo "<p><u>We encourage you to follow us on Twitter</u><br><br>";
?>
<a href="https://twitter.com/groupidentity" class="twitter-follow-button" data-show-count="false" data-lang="en" data-size="large">Follow @GroupIdentity</a></p>

<!--

/*       You have been entered into the drawing. */
/*       so that we can direct message you if you */
/*       win, however, it is not necessary to follow us to be in the */
/*       drawing. Should you win, we can always mention you and you can */
/*       respond to our mention with the address to send the prize to. */

	<p>If you agreed to participate in the experimental portion of the
	  study, we will be in contact on Twitter. If you would like to
	  participate in the experiment and did not indicate this on the
	  initial consent form, you may partipate by clicking on the
	  following link:</p>
-->    
	<h3 class="center-title"> HELP SPREAD THE WORD</h3>
	<span> We hope you share this study with your followers on
	Twitter!  Click the "Tweet" button to share!</span>
	
        <span style="margin-left:10px;"><a href="https://twitter.com/share" class="twitter-share-button"
	   data-lang="en" data-count="none" data-size="large" 
	   data-url='http://smallsocialsystems.com/asaf/AboutUs.html?flag=<?php echo $_SESSION["username"]; ?>_child'
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
