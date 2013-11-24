<?php
session_start();
// Get data for accessing database
require_once('../safe/config.inc');
global $dbh;

// Get flag from input, write to db
// store referrer in session variable
$_SESSION['flag'] = $flag = isset($_GET['flag']) ? $_GET['flag'] : null;

$rqst = $dbh->prepare("INSERT INTO visitors SET username=:uname");
$rqst->bindParam(':uname',$flag, PDO::PARAM_STR);
$rqst->execute();

$_SESSION['userid'] = $userid = isset($_SESSION['userid']) ? $_SESSION['userid'] : bin2hex(openssl_random_pseudo_bytes(16));


?>
<html>
<head>
<title>Group Identity Project</title>
<script src="core/jquery-ui-1.8.21.custom/js/jquery-1.7.2.min.js" type="text/javascript"></script>
<script src="core/jquery-ui-1.8.21.custom/js/jquery-ui-1.8.21.custom.min.js" type="text/javascript"></script>
<script type="text/javascript"> $("button").button(); </script>
<script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src="//platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");</script>
<link rel="shortcut icon" href="core/images/idproj.ico" type="image/x-icon" />
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

<div class="container">
  <div class="center column">
    <div class="center-section">
      <div class="center-title">Group Identities</div>
      <div class="center-para">
	Every human being, from every walk of life, belongs to multiple social groups. 
    We belong to a family, to a city, to a country, to a culture. People join other 
    groups, fraternities, social clubs, activity groups, sports teams. All of the groups 
    we belong to in some way defines who we are, but not all groups are equally important
    to our self-identity. The groups we identify most strongly with have a bigger sway on 
    our behavior&mdash;and this is what we hope to detect through Twitter.
      </div>
    </div>
    <div class="center-section">
      <div class="center-title">About the Project</div>
      <div class="center-para">
	In this study, we plan to build a system that uses a person's
	Twitter account to infer the groups with whom that person
	identifies.  For example, using a person's tweets we will guess
	whether the person identifies with a particular political party or
	sports team and how strongly they identify with the group. We
	hypothesize there is a direct relationship between the tweets a
	person reads and shares&mdash;that is, how information flows from
	person to person&mdash;and the groups with whom he or she
	identifies.
      </div>
    </div>
    <div class="center-section">
      <div class="center-title">Who Can Participate</div>
      <div class="center-para">
	 Anyone with a Twitter account can participate.  If you are an IU student and want to get credit for participating in an experiment, click the <span style="color:red">RED</span> participate button below.  Otherwise, click the <span style="color:#FC0">GOLD</span> participate button below.
      </div>
    </div>
    <button id="participate-button" class="ui-button ui-button-text-only ui-widget ui-state-default
	ui-corner-all" onClick="document.location.href='IUConsent.php';" style="background:red;color:#FDFEE4">
	 <span class="ui-button-text">Participate!<br>(IU student)</span>
    </button>
    <button id="participate-button" class="ui-button ui-button-text-only ui-widget ui-state-default
	ui-corner-all" onClick="document.location.href='Consent.php';">
	 <span class="ui-button-text">Participate!<br>(non-IU student)</span>
    </button>
  </div>
  <div class="left column">
    <div class="bio">
      <img src="core/images/winter.jpg" class="headshot">
      <div class="bio-text">
	<b>Dr. Winter Mason</b> is a Data Scientist at Facebook.  His research focuses
	on social networks, social media, and crowdsourcing.
      </div>
    </div>
    <div class="bio">
      <img src="core/images/asaf.jpg" class="headshot">
      <div class="bio-text">
	<b>Asaf Beasley</b> is a graduate student in Social Psychology and
	Cognitive Science at <a href="http://www.iub.edu">Indiana
	University</a>, working
	with <a href="http://www.indiana.edu/~soccog/home.html">Eliot
	Smith</a>. His research interests include social dynamics and
	intergroup behavior.
      </div>
    </div>
  </div>
  <div class="right column">
    <div class="uni-logos">
      <a href="http://www.iub.edu"><img src="core/images/iu_logo.jpg" class="uni"></a>
    </div>
  </div>
</div>

<div class="footer">
<div id="contact-info">
  For more information, contact:<br>
  Group Identity Project<br>
  group.id.project [at] gmail.com<br><br>
<a href="https://twitter.com/GroupID_Project" class="twitter-follow-button" data-show-count="false" data-lang="en" data-size="large">Follow @GroupIdentity</a>
</div>
</div>

</body>
</html>
