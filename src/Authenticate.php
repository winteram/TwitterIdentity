<?php
/* Start session and load library. */
session_start();
require_once('core/twitteroauth/twitteroauth.php');
require_once('core/safe/config.inc');

/* Get survey credentials */
$agree = $_GET['agree'];
$agree2 = $_GET['agree2'];

/* Build TwitterOAuth object with client credentials. */
$connection = new TwitterOAuth(CONSUMER_KEY, CONSUMER_SECRET);

/* Get temporary credentials. */
$request_token = $connection->getRequestToken();

/* Save temporary credentials to session. */
$_SESSION['oauth_token'] = $token = $request_token['oauth_token'];
$_SESSION['oauth_token_secret'] = $request_token['oauth_token_secret'];

 
/* If last connection failed don't display authorization link. */
switch ($connection->http_code) {
  case 200:
    /* Build authorize URL and redirect user to Twitter. */
    $url = $connection->getAuthorizeURL($token, FALSE);
    header('Location: ' . $url . '&agree=' . $agree . '&agree2=' . $agree2); 
    break;
  default:
    /* Show notification if something went wrong. */
    echo 'Could not connect to Twitter. Refresh the page or try again later.  value = '.print_r($connection);
    session_destroy();
}

?>