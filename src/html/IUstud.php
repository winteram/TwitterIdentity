<?php
session_start();
// Get data for accessing database
require_once('../safe/config.inc');
global $dbh;

// Get flag from input, write to db
$flag = isset($_GET['flag']) ? $_GET['flag'] : "unknown";

$rqst = $dbh->prepare("INSERT INTO visitors SET username=:uname");
$rqst->bindParam(':uname',$flag, PDO::PARAM_STR);
$rqst->execute();

// store referrer in session variable
$_SESSION['flag'] = $flag;

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

<h2 style="text-align:center">&nbsp; </h2>
<h2 style="text-align:center">Are you an Indiana Unversity student?

</h2>

<div style = text-align:center> <button style="width:80px;height:30px" id="yes_student" onClick="document.location.href='IUConsent.php';"> YES </button> 
  &nbsp; &nbsp;  &nbsp;  &nbsp;      
  <button style="width:80px;height:30px" id ="no_student" onClick="document.location.href='Consent.php';"> NO </button>

</div>
  
 

</body>
</html>
