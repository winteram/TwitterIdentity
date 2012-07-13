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
    if($("#agree").is(':checked'))
	{ agree = true; }
    if($("#agree2").is(':checked'))
	{ agree2 = true; }
    if(!agree) {
	$("#error_consent").html("Please indicate you have read the information on this page and agree to participate in the study by checking the first box above");
    } else {
	window.location.href = "Authenticate.php?agree=" + (agree ? 1 : 0) + "&agree2=" + (agree2 ? 1 : 0);
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

<h2 style="text-align:center">INFORMED CONSENT</h2>


<h4>1. The purpose of this research is:</h4>
<div>The groups with whom a person identifies are strongly tied to that person's
emotions, beliefs, and behaviors.  In this study, we hope to accomplish two
things.  The first is to build a system that uses a person's Twitter
account to infer the groups with whom that person identifies.  For example,
using a person's tweets we will guess whether the person identifies with a
particular political party or sports team and how strongly they identify
with the group. We hypothesize there is a direct relationship between the
tweets a person reads and shares—that is, how information flows from person
to person—and the groups with whom he or she identifies.</div>

<h4>2. The general plan of the research is:</h4>
<div>We will collect information on the groups with whom Twitter users identify
and how strongly they identify with these groups.  We will then collect
those users’ public tweets and profile information, as well as the public
tweets and profile information of their friends and followers.  We will use
this information to build a model that attempts to predict the
participants’ groups and how strongly they identify with those groups.  For
those participants who also agree to participate in an additional phase of
the study, we will ask them to post a tweet containing information relevant
to a particular group, so we can further understand the relationship
between group identity and information flow.</div>

<h4>3. The following procedures will be performed on those who participate in
this research:</h4>
<div>If you agree to participate in the first part of this study, we will ask
you to complete a survey about the groups with whom you identify and how
strongly you identify with those groups.  We will then crawl the public
information on Twitter to obtain your recent tweets, your public profile
information, and the public tweets and profile information of your friends
and followers.</div>

<div>If you agree to participate in the second part of the study, we will
ask you to follow our Twitter account, <a
href="https://twitter.com/#!/GroupIdentity">@GroupIdentity</a>.  In 1-3
months we will send you a direct message through Twitter asking you to post
a tweet with a URL that will be relevant to some group (though not
necessarily a group you identify with). We will then observe whether and
how your followers share the information in the tweet.</div> <div>As a
reminder, you may refuse to participate in this study at any time.</div>


<h4>4. Those who participate in this research will be asked to do the
following things:</h4> <div>By consenting to participate in this study you
agree to allow us to download your public tweets for the last 3 months and
the following 3 months, as well as profile information such as who your
friends and followers are.  This information will be stored in a secure
manner and will only be viewed by us, or presented in an aggregated manner
that does not reveal specific information about you.</div> <div>You can
also agree to participate in the second phase of this study, by checking
the box that says, "I agree to be contacted by the researchers through
Twitter" and following our Twitter account, <a
href="https://twitter.com/#!/GroupIdentity">@GroupIdentity</a>.  In this
extension, we will ask you to post a tweet containing a URL relevant to a
particular group identity, so we can observe how your followers share
it.</div>

<h4>5. This research may result in the following discomforts:</h4>
<div>It is not expected that participation in this study will result in any
discomforts.  All information you provide in the survey will be kept in the
strictest confidence, and no personally identifying information about you
will be seen by anyone other than the researchers involved in this study.
If you participate in the second part of the study, you will be given the
opportunity to preview the tweet and may refuse to tweet it with no
consequence.</div>

<h4>6. Participation in this research may involve the following risks:</h4>
<div>There are no anticipated risks from participating in this study.</div>

<div>The investigators will do everything possible to prevent or reduce
discomfort and risk, but it is not possible to predict everything that
might occur. If a participant has unexpected discomfort or thinks something
unusual or unexpected is occurring, he/she should contact:</div>

<div class="consent-contact">
<span>Dr. Winter Mason<br>
Stevens Institute of Technology<br>
(201) 216-3312<br>
wmason [at] stevens [dot] edu</span>
</div>

<div>The investigators will assure that any data or answers to questions will
remain confidential with regard to the subject's identity.</div>

<div>Anyone who agrees to participate in this research may change his/her mind
at any time. Refusal to participate or to continue to participate will not
harm an individual's relationship with the investigators or the
University. In the event of injury resulting from any research procedure,
the subject may obtain information from:</div>


<div class="consent-contact">
<span>Zvi Aronson, Head, IRB<br>
WJHSTM, Stevens Institute of Technology<br>
Telephone: (201) 216 -5032.</span>
</div>

<div id="consent-form-box">
<form name="consent">

<div><input type="checkbox" id="agree" name="agree"/> By checking this box, I am
indicating that I have read the above description of a research project; I
am older than 18 years of age; I have had all of my questions answered to
my satisfaction; and I agree to participate in this research.</div>

<div><input type="checkbox" id="agree2" name="agree2"/> By checking this box, I agree
to be contacted by the researchers through a direct message on Twitter; I
agree to review a tweet and consider posting the message on behalf of the
researchers.</div>

<div>By checking the box(es) above and clicking the link below, you will be
digitally signing this document.  You will be asked to authenticate your
account through Twitter to demonstrate you are the owner of your Twitter
account and grant us permission to retrieve information about your profile
and tweets from your account.</div>

<div id="error_consent" class="error"></div>
<div id="sign-in"><img src="core/images/lighter.png" alt="Sign in with Twitter" onClick="verify_consent();"/></div>
</form>
</div>

<div>The Institutional Review Board of Stevens Institute of Technology has
reviewed and approved this study on the following
  date: June 25, 2012 >


</div>

</body>
</html>
