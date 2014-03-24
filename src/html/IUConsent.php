<?php
session_start();
require_once('core/fb-php/src/facebook.php');
require_once('../safe/config.inc');

$_SESSION['userid'] = $userid = isset($_SESSION['userid']) ? $_SESSION['userid'] : bin2hex(openssl_random_pseudo_bytes(16));
$_SESSION['IU'] = 1;
$fb_loggedin = isset($_SESSION['fb_status']) ? "core/img/checkbox_checked.png" : "core/img/checkbox_unchecked.png";
$tw_loggedin = isset($_SESSION['tw_status']) ? "core/img/checkbox_checked.png" : "core/img/checkbox_unchecked.png";
$fb_verified = isset($_SESSION['fb_status']) ? 1 : 0;
$tw_verified = isset($_SESSION['tw_status']) ? 1 : 0;

$config = array(
      'appId' => APP_ID,
      'secret' => APP_SECRET,
      'fileUpload' => false, // optional
      'allowSignedRequest' => false, // optional, but should be set to false for non-canvas apps
  );

$facebook = new Facebook($config);
$par['scope'] = "offline_access,
                    user_groups,
                    friends_groups,
                    user_interests,
                    friends_interests,
                    user_likes,
                    friends_likes,
                    user_religion_politics,
                    friends_religion_politics,
                    user_status,
                    friends_status,
                    read_stream";
$par['redirect_uri'] = 'http://smallsocialsystems.com/groupid/FBAuth.php';
$loginUrl = $facebook->getLoginUrl($par);
?>

<html>
<head>
<title>Self Aspects in Social Media</title>
<script src="core/jquery-ui-1.8.21.custom/js/jquery-1.7.2.min.js" type="text/javascript"></script>
<script src="core/jquery-ui-1.8.21.custom/js/jquery-ui-1.8.21.custom.min.js" type="text/javascript"></script>
<script> $(document).ready(function() {
    $( "#error_popup" ).dialog({
      autoOpen: false,
      resizable: false,
      modal: true
    });
  });
</script>
<script type="text/javascript">
function verify_consent(once) 
{
    once = typeof once !== 'undefined' ? once : false; // This line sets once to false if not defined
    var agree = false;
    var error = false;
    var errormsg = "";
    var fb_verified = <?php echo $fb_verified; ?>;
    var tw_verified = <?php echo $tw_verified; ?>;
    var verified = fb_verified + tw_verified;
    var IUname = $("#IUName").val();

    if($("#agree").is(':checked')) { agree = true; }

    if (verified==0) {
      errormsg += "<p>Please log in with a Twitter and/or Facebook account</p>";
      error=true;
    } 
    if(!agree) {
      errormsg += "<p>Please indicate you have read the information on this page and agree to participate in the study by checking the first box above</p>";
      error=true;
    } 
    if( IUname.length < 3) {
      errormsg += "<p> Please indicate your IU username in the text box above <p>";
      error=true;
    }

    if(error==false && verified==2 || verified==1 && once==true) {
      window.top.location.href = "IdentitySurvey.php?agree=" + (agree ? 1 : 0) + "&IUname=" + IUname;
    } else if (error==true) {
      $('#error_popup').html(errormsg);
      $('#error_popup').dialog( "option", "buttons", [
        {
          text: "Cancel",
          click: function() {
            $( this ).dialog( "close" );
          }
        }
      ]);
      $('#error_popup').dialog("open");
    } else if (verified==1) {
      errormsg = "You are only logged in with ";
      errormsg += fb_verified==1 ? "Facebook." : "Twitter.";
      errormsg += " If you have a ";
      errormsg += fb_verified==1 ? "Twitter " : "Facebook ";
      errormsg += "account, please hit cancel and log in with that account as well.";
      $('#error_popup').html(errormsg);
      $('#error_popup').dialog( "option", "buttons", [
        {
          text: "Continue",
          click: function() {
            verify_consent(true);
          }
        },
        {
          text: "Cancel",
          click: function() {
            $( this ).dialog( "close" );
          }
        }
      ]);
      $('#error_popup').dialog("open");
    }
}
</script>
<link rel="shortcut icon" href="core/img/idproj.ico" type="image/x-icon" />
<link rel='stylesheet' type='text/css'
      href='core/jquery-ui-1.8.21.custom/css/pepper-grinder/jquery-ui-1.8.21.custom.css' />
<link rel='stylesheet' type='text/css' href='core/css/IdentitySurvey.css' />
</head>
<body bgcolor="#F5F3EF">
<div class="header"> 
  <span id="idproj-hdr"><img src="core/img/idproj.jpg">
  <img src="core/img/Aspects_Cover.png" alt="Self Aspects in Social Media"></span>
</div>

<?php
   if( isset($_GET['error']) ) {
     if( $_GET['error']==1) {
       echo "<div class='error'> We're sorry, there was a problem with the oAuth
       in Twitter.  Please ensure you have cookies enabled for this site.
       Scroll to the bottom of the page to try again. </div>";
     }
     else {
       echo "<div class='error'> We're sorry, there was a problem with the
       authentication through Twitter.  Please try again. </div>";
     }
   }
?>
<div id="consent-form">
<h2 style="text-align:right">Study #1208009352</h2>
<h2 style="text-align:center">INDIANA UNIVERSITY INFORMED CONSENT STATEMENT FOR</h2>
<h2 style="text-align:center">Self Aspects in Social Media</h2>

<p>

You are invited to participate in a research study of how people express aspects
of themselves with Social Media. You were selected as a possible subject because
you are currently enrolled in P101/102//151/P152.  We ask that you read this
form and ask any questions you may have before agreeing to be in the study.

</p>

<h4> STUDY PURPOSE: </h4>

<div> 

Other researchers have used data from Twitter to draw conclusions about the
public&rsquo;s moods and emotions.  We hope to use Twitter data to learn about
the groups with which people identify.  For example, a person&rsquo;s tweets may
contain clues indicating that they identify with a particular political party or
sports team. We hypothesize there is a direct relationship between the tweets a
person reads and shares&mdash;that is, how information flows from person to
person&mdash;and the groups with whom he or she identifies.

</div>

<p><strong>

NUMBER OF PEOPLE TAKING PART IN THE STUDY:

</strong></p>

<p>

If you agree to participate, you will be one of 3000 subjects who will be
participating in this research.

</p>

<h4>

PROCEDURE FOR THE STUDY:

</h4>

<div><strong>

If you agree to participate in the first part of this study, we will ask you to
complete a survey on aspects of yourself, such as important domains of your
life, groups you identify with, and how you use Twitter and Facebook. </strong>.
We will then examine publicly available information on Twitter to obtain your
recent tweets, your public profile information, and the public tweets and
profile information of your friends and followers. With your consent we will
also use information from your Facebook profile, such as status updates, likes,
and groups.

</div>

<div> <strong>

By consenting to participate in this study you agree to allow us to download
your public tweets for the last 3 months and the following 3 months, as well as
Facebook profile information.  </strong>. This information will be stored in a
secure manner and will only be viewed by us, or presented in an aggregated
manner that does not reveal specific information about you or your friends and
followers. We will not have access to any private messages, nor will we ever
view any pictures of you, or link your name to your profile. The information we
gather is typical information gathered by an app you authorize on Facebook or
Twitter. All user names will be encrypted to help ensure that your responses
remain confidential at every stage of the study. All Twitter and Facebook
usernames will be obscured using an encryption technique called a one-way
hashing algorithm. The encryption key will remain confidential and separate from
the data obtained. The survey responses and data acquired from Twitter will only
be tied to the encrypted identity, which will appear as meaningless symbols in
the absence of the encryption key.

</div> 


<h4> RISKS IN TAKING PART IN THE STUDY: </h4> 

<p> While on the study, the risks are: </p>

<div>
<strong>

It is not expected that participation in this study will result in any
significant risks.</strong> All information you provide in the survey will be
kept in the strictest confidence, and no personally identifying information
about you will be seen by anyone other than the researchers involved in this
study.  If you participate in the second part of the study, you will be given
the opportunity to preview the tweet and may refuse to tweet it with no
consequence.

If for any reason you feel uncomfortable answering any question on the survey,
you can skip it and you will still receive experiment credit.


</div>


<h4>

BENEFITS OF TAKING PART IN THE STUDY:

</h4>
<div>
  <p>

  The benefits to participation that are reasonable to expect are:<br> 

  A better understanding of social psychology research, an experimental credit,
  and, hopefully, this gets you thinking about how you express your identities
  in online social networks like Twitter and Facebook.

  </p>
</div>

<p><strong>

ALTERNATIVES TO TAKING PART IN THE STUDY:

</strong></p>
<p>

Instead of being in the study, you may either participate in a different study,
or complete the requisite paper(s) as determined by your instructor.

</p>
<p><strong>

CONFIDENTIALITY

</strong></p>
<p>

Efforts will be made to keep your personal information confidential.  We cannot
guarantee absolute confidentiality.  Your personal information may be disclosed
if required by law.  Your identity will be held in confidence in reports in
which the study may be published and databases in which your results may be
stored.

</p>
<p>

Organizations that may inspect and/or copy your research records for quality
assurance and data analysis include groups such as the study investigator and
his/her research associates, the IUB Institutional Review Board or its
designees, the study sponsor, and (as allowed by law) state or federal agencies,
specifically the Office for Human Research Protections (OHRP) who may need to
access your research records.

</p>
<p><strong>COSTS</strong></p>
<p>

Taking part in this study will not lead to added costs to you. 

</p>
<p><strong>PAYMENT</strong></p>
<p>

You will receive one experimental credit for taking part in this study.

</p>
<p><strong>CONTACTS FOR QUESTIONS OR PROBLEMS</strong></p>
<p>

For questions about the study or a research-related injury, contact the
researcher Eliot Smith at (812) 856-0196. If you cannot reach the researcher
during regular business hours (i.e. 8:00AM-5:00PM), please call the IU Human
Subjects Office at (812) 856-4242.

</p>
<p>

For questions about your rights as a research participant or to discuss
problems, complaints or concerns about a research study, or to obtain
information, or offer input, contact the IU Human Subjects Office (812) 856-4242
or by email at irb@iu.edu

</p>
<p><strong>VOLUNTARY NATURE OF STUDY</strong></p>
<p>

Taking part in this study is voluntary. You may choose not to take part or
may leave the study at any time. Leaving the study will not result in any
penalty or loss of benefits to which you are entitled. Your decision
whether or not to participate in this study will not affect your current or
future relations with the researchers or the university.

</p>
<p><strong>SUBJECT&rsquo;S CONSENT</strong></p>
<p>

In consideration of all of the above, I give my consent to participate in this
research study.

</p>
<p>

I will be emailed a copy of this consent for my records. I agree to take part in
this study.

</p>
<div id="consent-form-box">
  <form name="consent">
    You will be asked to authenticate your account through Twitter and/or Facebook through the links below.
    <div class ="error" id="error_popup"></div>
    <div class='sign-in'>
      <img id="fb-check" src=<?php echo $fb_loggedin; ?> width="40" height="40" />
      <a href=<?php echo $loginUrl;?> > <img src="core/img/fb-login-button.png" alt="Sign in with Facebook"/></a>
    </div>
    <div class="sign-in">
      <img id="tw-check" src=<?php echo $tw_loggedin; ?> width="40" height="40" />
      <a href="Authenticate.php"> <img src="core/img/lighter.png" alt="Sign in with Twitter"/> </a>
    </div>


    <div><input type="checkbox" id="agree" name="agree"/>

    By checking this box, I am indicating that I have read the above description of
    a research project; I am older than 18 years of age; I have had all of my
    questions answered to my satisfaction; and I agree to participate in this
    research.

    </div>

    <div>
      <p>

      So that we know you read the consent and may assign you experimental credit, please complete the fields below.

      </p>
      <p>

      IU Username: <input type = "text" id = "IUName" name = "IUName" />

      </p>
      <p>

    By clicking a link and checking the above box, you will be digitally
    signing this document.
      </p>

    <div class='sign-in'>
      <input type="button" value="Continue to survey" onClick="verify_consent();"/>
    </div>

    </div>
  </form>
</div>

<div class="center"><img src="core/img/ICSstamp.png" alt="IRB approval stamp" style="max-width:250px;"/></div>
</div>
</body>
</html>
