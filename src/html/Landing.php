<?php 
session_start();
require_once('core/twitteroauth/twitteroauth.php');
require_once('core/safe/config.inc');
global $dbh;
 
// If the oauth_token is old redirect to the connect page. 
if (isset($_REQUEST['oauth_token']) && $_SESSION['oauth_token'] !== $_REQUEST['oauth_token']) {
   $_SESSION['oauth_status'] = 'oldtoken';
   session_destroy();
   header('Location: ./Consent.php?error=1');
}

// Create TwitteroAuth object with app key/secret and token key/secret from default phase 
$connection = new TwitterOAuth(CONSUMER_KEY, CONSUMER_SECRET,
			       $_SESSION['oauth_token'], $_SESSION['oauth_token_secret']);

// Request access tokens from twitter 
$access_token = $connection->getAccessToken($_REQUEST['oauth_verifier']);
//print_r($access_token);

// Remove no longer needed request tokens 
unset($_SESSION['oauth_token']);
unset($_SESSION['oauth_token_secret']);

// If HTTP response is 200 continue otherwise send to connect page to retry
$_SESSION['username'] = "Failure";

// If successful
if (200 == $connection->http_code) {
  // The user has been verified and the access tokens can be saved for future use 
  $_SESSION['status'] = 'verified';
  $connection = new TwitterOAuth(CONSUMER_KEY, CONSUMER_SECRET, $access_token['oauth_token'], $access_token['oauth_token_secret']);
  $user = $connection->get('account/verify_credentials');

  // Keep username in session variables
  $_SESSION['username'] = $user->screen_name;
  $username = $_SESSION['username'];

  // put responses to consent form in dB
  $agree1 = isset($_SESSION['agree']) ? intval($_SESSION['agree']) : 0;
  $agree2 = isset($_SESSION['agree2']) ? intval($_SESSION['agree2']) : 0;
  $flag = isset($_SESSION['flag']) ? $_SESSION['flag'] : "NULL";


  // Check if survey exists for username
  $rqst = $dbh->prepare("SELECT username FROM survey WHERE username=:uname");
  $rqst->bindParam(':uname',$username, PDO::PARAM_STR);
  $row = $rqst->execute();
  $result = $rqst->fetch(PDO::FETCH_ASSOC);

  // if username exists, it will match
  if ($result['username'] === $username) {
    $query = "UPDATE authentic SET access_token=:token, access_secret=:secret, agree1=:agree1, agree2=:agree2, referred_by=:flag WHERE username=:uname";
  } 
  else {
    $rqst1 = $dbh->prepare("INSERT INTO survey SET username=:uname, started=NOW()");
    $rqst1->bindParam(':uname',$username, PDO::PARAM_STR);
    $rqst1->execute();
    $query = "INSERT INTO authentic SET username=:uname, access_token=:token, access_secret=:secret, agree1=:agree1, agree2=:agree2, referred_by=:flag";
  }

  $rqst2 = $dbh->prepare($query);
  $rqst2->bindParam(':uname',$username, PDO::PARAM_STR);
  $rqst2->bindParam(':token',$access_token['oauth_token'], PDO::PARAM_STR);
  $rqst2->bindParam(':secret',$access_token['oauth_token_secret'], PDO::PARAM_STR);
  $rqst2->bindParam(':agree1',$agree1, PDO::PARAM_INT);
  $rqst2->bindParam(':agree2',$agree2, PDO::PARAM_INT);
  $rqst2->bindParam(':flag',$flag, PDO::PARAM_STR);
  $rqst2->execute();

  // Send them to the survey
  header('Location: ./IdentitySurvey.php');
} else {
  // Save HTTP status for error dialog on connnect page.
  session_destroy();
  header('Location: ./Consent.php?error=1');
}

?>