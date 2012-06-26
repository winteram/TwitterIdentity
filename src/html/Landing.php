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
print_r($access_token);

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

  // put responses to consent form in dB
  $agree1 = isset($_SESSION['agree']) ? intval($_SESSION['agree']) : 0;
  $agree2 = isset($_SESSION['agree2']) ? intval($_SESSION['agree2']) : 0;

  // Check if survey exists for username
  $rqst = $dbh->prepare("SELECT username FROM survey WHERE username=:uname");
  $rqst->bindParam(':uname',$username, PDO::PARAM_STR);
  $user = $rqst->execute();

  // if username exists, it will match
  if ($user == $username) {
    $query = "UPDATE survey SET agree1=:agree1, agree2=:agree2 WHERE username=:uname";
  } else {
    $query = "INSERT INTO survey SET username=:uname, agree1=:agree1, agree2=:agree2, started=NOW()";
  }

  $rqst = $dbh->prepare($query);
  $rqst->bindParam(':uname',$username, PDO::PARAM_STR);
  $rqst->bindParam(':agree1',$agree1, PDO::PARAM_INT);
  $rqst->bindParam(':agree2',$agree2, PDO::PARAM_INT);
  $rqst->execute();

  // Send them to the survey
  header('Location: ./IdentitySurvey.php');
} else {
  // Save HTTP status for error dialog on connnect page.
  session_destroy();
  header('Location: ./Consent.php?error=1');
}

?>