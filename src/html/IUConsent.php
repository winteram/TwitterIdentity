<?php
session_start();
?>

<html>
<head>
<title>Group Identities on Twitter</title>
<script src="core/jquery-ui-1.8.21.custom/js/jquery-1.7.2.min.js" type="text/javascript"></script>
<script src="core/jquery-ui-1.8.21.custom/js/jquery-ui-1.8.21.custom.min.js" type="text/javascript"></script>
<script type="text/javascript">
function verify_consent() 
{
    var agree = false;
    var agree2 = false;
    var IUname = $("#IUName").val();
    var error = false
    var errormsg = ""
	       	
    if($("#agree").is(':checked'))
	{ 
	  agree = true;
	}
    if(!agree)
      {
	error = true; 
	errormsg += "<p> Please indicate you have read the information on this page and agree to participate in the study by checking the first box above <p>"
      }    
    if($("#agree2").is(':checked')) 
      { 
	agree2 = true;  
      }

    if( IUname.length < 3)
      {
	errormsg += "<p> Please indicate your IU username in the text box above <p>";
	error=true;
      }
	
    if(error==true) {
      $("#error_consent").html(errormsg)
    } else {
      var redirect = "Authenticate.php?agree=" + (agree ? 1 : 0) + "&agree2=" + (agree2 ? 1 : 0);
      redirect += "&IUname=" + IUname;
      window.location.href = redirect;
    }        
}
</script>
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

<?php
   if( isset($_GET['error']) ) {
     if( $_GET['error']==1) {
       echo "<div class='error'> We're sorry, there was a problem with the oAuth in Twitter.  Please ensure you have cookies enabled for this site.  Scroll to the bottom of the page to try again. </div>";
     }
     else {
       echo "<div class='error'> We're sorry, there was a problem with the authentication through Twitter.  Please try again. </div>";
     }
   }
?>
<div id="consent-form">
  <h2 style="text-align:right">Study #1208009352</h2>
<h2 style="text-align:center">INDIANA UNIVERSITY INFORMED CONSENT STATEMENT FOR</h2>
<h2 style="text-align:center">Group Identities on Twitter</h2>
<p>You are invited to participate in a research study of how people express their group identities on Twitter. You were selected as a possible subject because you are currently enrolled in P101/102//151/P152.<br>
&nbsp;We ask that you read this form and ask any questions you may have before agreeing to be in the study. </p>
The study is being conducted by Dr. Eliot Smith at Indiana University.
<h4>STUDY PURPOSE:</h4>
<div> Other researchers have used data from Twitter to draw conclusions about the public’s moods and emotions.  We hope to use Twitter data to learn about the groups with which people identify.  For example, a person’s tweets may contain clues indicating that they identify with a particular political party or sports team. We hypothesize there is a direct relationship between the tweets a person reads and shares—that is, how information flows from person to person—and the groups with whom he or she identifies.</div>

<p><strong>NUMBER OF PEOPLE TAKING PART IN THE STUDY:</strong></p>
<p>If you agree to participate, you will be one of 800 subjects who will be participating in this research.</p>
<div></div>

<h4>PROCEDURE FOR THE STUDY:</h4>
<div><strong>If you agree to participate in the first part of this study, we will ask you to complete a survey about the groups with whom you identify and how strongly you identify with those groups</strong>. We will then examine publicly available information on Twitter to obtain your recent tweets, your public profile information, and the public tweets and profile information of your friends and followers.</div>

<div> <strong>By consenting to participate in this study you agree to allow us to download your public tweets for the last 3 months and the following 3 months, as well as profile information such as who your friends and followers are</strong>. This information will be stored in a secure manner and will only be viewed by us, or presented in an aggregated manner that does not reveal specific information about you or your friends and followers. All user names will be encrypted to help insure that your responses remain confidential at every stage of the study. All twitter usernames will be obscured using an encryption technique  called a one-way hashing algorithm. The encryption key will remain confidential and separate from the data obtained. The survey responses and data acquired from Twitter will only be tied to the encrypted identity, which will appear as meaningless symbols in the absence of the encryption key.</div> 

<div> <strong>You can also agree to participate in the second phase of this study</strong>, by checking the box that says, "I agree to be contacted by the researchers through Twitter" and following our Twitter account, @GroupID_Project.  <strong>In this part of the study, within the next 2-3 months we will send you a direct message asking you to post a tweet containing a URL relevant to a particular group identity</strong>, so we can observe how your followers share it.  While our research goals will benefit if you participate in this second part of the study, you always have the right to discontinue your participation in this study at any time. </div>


<h4>RISKS IN TAKING PART IN THE STUDY:</h4> <p> While on the study, the risks are:</p>
<div>
<strong>It is not expected that participation in this study will result in any significant risks.</strong> All information you provide in the survey will be kept in the strictest confidence, and no personally identifying information about you will be seen by anyone other than the researchers involved in this study.  If you participate in the second part of the study, you will be given the opportunity to preview the tweet and may refuse to tweet it with no consequence.
</div>


<h4>BENEFITS OF TAKING PART IN THE STUDY:</h4>
<div>
  <p>The benefits to participation that are reasonable to expect are:<br>
    A better understanding of social psychology research, an experimental credit, and, hopefully, this gets you thinking about how you express your identities in online social networks like Twitter. </p>
</div>

<p><strong>ALTERNATIVES TO TAKING PART IN THE STUDY:</strong></p>
<p>Instead of being in the study, you may either participate in a different study, or complete the requisite paper(s) as determined by your instructor.</p>
<p><strong>CONFIDENTIALITY</strong></p>
<p>Efforts will be made to keep your personal information confidential.&nbsp; We cannot guarantee absolute confidentiality.&nbsp; Your personal information may be disclosed if required by law.&nbsp; Your identity will be held in confidence in reports in which the study may be published and databases in which your results may be stored. </p>
<p>Organizations that may inspect and/or copy your research records for quality assurance and data analysis include groups such as the study investigator and his/her research associates, the IUB Institutional Review Board or its designees, the study sponsor, and (as allowed by law) state or federal agencies, specifically the Office for Human Research Protections (OHRP) who may need to access your research records.</p>
<p><strong>COSTS</strong></p>
<p>Taking part in this study will not lead to added costs to you. </p>
<p><strong>PAYMENT</strong></p>
<p>You will receive one experimental credit for taking part in this study.</p>
<p><strong>CONTACTS FOR QUESTIONS OR PROBLEMS</strong></p>
<p>For questions about the study or a research-related injury, contact the researcher Eliot Smith at (812) 856-0196. If you cannot reach the researcher during regular business hours (i.e. 8:00AM-5:00PM), please call the IU Human Subjects Office at (812) 856-4242.</p>
<p>For questions about your rights as a research participant or to discuss problems, complaints or concerns about a research study, or to obtain information, or offer input, contact the IU Human Subjects Office (812) 856-4242 or by email at irb@iu.edu</p>
<p><strong>VOLUNTARY NATURE OF STUDY</strong></p>
<p>Taking part in this study is voluntary.&nbsp; You may choose not to take part or may leave the study at any time.&nbsp; Leaving the study will not result in any penalty or loss of benefits to which you are entitled.&nbsp; Your decision whether or not to participate in this study will not affect your current or future relations with the researchers or the university. </p>
<p><strong>SUBJECT&rsquo;S CONSENT</strong></p>
<p>In consideration of all of the above, I give my consent to participate in this research study.&nbsp; </p>
<p>I will be emailed a copy of this consent for my records. I agree to take part in this study.</p>
<div></div>
<div id="consent-form-box">
  <form name="consent">

<div><input type="checkbox" id="agree" name="agree"/>
   By checking this box, I am
indicating that I have read the above description of a research project;  I have had all of my questions answered to
my satisfaction; and I agree to participate in this research.</div>

<div><input type="checkbox" id="agree2" name="agree2"/> By checking this box, I agree
to be contacted by the researchers through a direct message on Twitter; I
agree to review a tweet and consider posting the message on behalf of the
researchers.</div>

<div>
  <p>So that we know you read the consent and may assign you experimental credit, please complete the fields below.</p>
  <p>IU Username: <input type = "text" id = "IUName" name = "IUName" /></p>
  <p>By checking the box(es) above and clicking the link below, you will be digitally signing this document.&nbsp; You will be asked to authenticate your account through Twitter to demonstrate you are the owner of the Twitter account.</p>
</div>

<div id="error_consent" class="error"></div>
<div id="sign-in"><img src="core/images/lighter.png" alt="Sign in with Twitter" onClick="verify_consent();"/></div>
</form>
</div>




</body>
</html>
