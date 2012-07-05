<?php 
session_start();
require_once('core/twitteroauth/twitteroauth.php');
require_once('../safe/config.inc');
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

// If successful
if (200 == $connection->http_code) {
  // The user has been verified and the access tokens can be saved for future use 
  $_SESSION['status'] = 'verified';
  $connection = new TwitterOAuth(CONSUMER_KEY, CONSUMER_SECRET, $access_token['oauth_token'], $access_token['oauth_token_secret']);
  $user = $connection->get('account/verify_credentials');

  // Keep twitter id in session variables
  $_SESSION['twitid'] = $user->id;
  $username = encode_salt($user->screen_name);
  $twitid = encode_salt($_SESSION['twitid']);

  // put responses to consent form in dB
  $agree1 = isset($_SESSION['agree']) ? intval($_SESSION['agree']) : 0;
  $agree2 = isset($_SESSION['agree2']) ? intval($_SESSION['agree2']) : 0;
  $flag = isset($_SESSION['flag']) ? $_SESSION['flag'] : "NULL";


  // Check if survey exists for twitter id
  $rqst = $dbh->prepare("SELECT Id FROM Survey WHERE Id=:twitid");
  $rqst->bindParam(':twitid',$twitid, PDO::PARAM_STR);
  $row = $rqst->execute();
  $result = $rqst->fetch(PDO::FETCH_ASSOC);

  // if username exists, it will match
  if ($result['twitid'] === $twitid) {
    $query = "UPDATE TwitterConnectionAccount SET AccessToken=:token, AccessTokenSecret=:secret, agree1=:agree1, agree2=:agree2, referred_by=:flag WHERE Id=:twitid";
    $rqst2 = $dbh->prepare($query);
    $rqst2->bindParam(':token',$access_token['oauth_token'], PDO::PARAM_STR);
    $rqst2->bindParam(':secret',$access_token['oauth_token_secret'], PDO::PARAM_STR);
    $rqst2->bindParam(':agree1',$agree1, PDO::PARAM_INT);
    $rqst2->bindParam(':agree2',$agree2, PDO::PARAM_INT);
    $rqst2->bindParam(':flag',$flag, PDO::PARAM_STR);
    $rqst2->bindParam(':twitid',$twitid, PDO::PARAM_STR);
    $rqst2->execute();
  } 
  else {
    // Add connection info
    $query = "INSERT INTO TwitterConnectionAccount SET Id=:twitid, AccountName=:uname, AccessToken=:token, AccessTokenSecret=:secret, agree1=:agree1, agree2=:agree2, referred_by=:flag";
    $rqst2 = $dbh->prepare($query);
    $rqst2->bindParam(':twitid',$twitid, PDO::PARAM_STR);
    $rqst2->bindParam(':uname',$username, PDO::PARAM_STR);
    $rqst2->bindParam(':token',$access_token['oauth_token'], PDO::PARAM_STR);
    $rqst2->bindParam(':secret',$access_token['oauth_token_secret'], PDO::PARAM_STR);
    $rqst2->bindParam(':agree1',$agree1, PDO::PARAM_INT);
    $rqst2->bindParam(':agree2',$agree2, PDO::PARAM_INT);
    $rqst2->bindParam(':flag',$flag, PDO::PARAM_STR);
    $rqst2->execute();

    $verified = $user->verified==1 ? 1 : 0;
    $geo = $user->geo_enabled==1 ? 1 : 0;
    $created_at = date("Y-m-d H:i:s",strtotime($user->created_at));
    //    echo $created_at;

    // Add Profile information
    $query = "INSERT INTO Profile (Id, name, screen_name, location, created_at, favourites_count, url, followers_count, lang, verified, profile_bgd_color, geo_enabled, description, time_zone, friends_count, statuses_count) VALUES (:twitid, :uname, :screenname, :location, :created_at, :fav_cnt, :url, :fol_cnt, :lang, :verified, :profile_bgd, :geo, :descrip, :tz, :frnd_cnt, :twt_cnt)";
    $rqst2 = $dbh->prepare($query);
    $rqst2->bindParam(':twitid',$twitid, PDO::PARAM_STR);
    $rqst2->bindParam(':uname',encode_salt($user->name), PDO::PARAM_STR);
    $rqst2->bindParam(':screenname',$username, PDO::PARAM_STR);
    $rqst2->bindParam(':location',$user->location, PDO::PARAM_STR);
    $rqst2->bindParam(':created_at',$created_at, PDO::PARAM_STR);
    $rqst2->bindParam(':fav_cnt',$user->favourites_count, PDO::PARAM_INT);
    $rqst2->bindParam(':url',$user->url, PDO::PARAM_STR);
    $rqst2->bindParam(':fol_cnt',$user->followers_count, PDO::PARAM_INT);
    $rqst2->bindParam(':lang',$user->lang, PDO::PARAM_STR);
    $rqst2->bindParam(':verified',$verified, PDO::PARAM_INT);
    $rqst2->bindParam(':profile_bgd',$user->profile_background_color, PDO::PARAM_STR);
    $rqst2->bindParam(':geo',$geo, PDO::PARAM_INT);
    $rqst2->bindParam(':descrip',$user->description, PDO::PARAM_STR);
    $rqst2->bindParam(':tz',$user->time_zone, PDO::PARAM_STR);
    $rqst2->bindParam(':frnd_cnt',$user->friends_count, PDO::PARAM_INT);
    $rqst2->bindParam(':twt_cnt',$user->statuses_count, PDO::PARAM_INT);
    $rqst2->execute();
    //  $rqst2->debugDumpParams();

    // Start survey
    $rqst1 = $dbh->prepare("INSERT INTO Survey SET Id=:twitid, username=:uname, started=NOW()");
    $rqst1->bindParam(':twitid',$twitid, PDO::PARAM_INT);
    $rqst1->bindParam(':uname',$username, PDO::PARAM_STR);
    $rqst1->execute();
  }

  // Send them to the survey
  header('Location: ./IdentitySurvey.php');
} else {
  // Save HTTP status for error dialog on connnect page.
  session_destroy();
  header('Location: ./Consent.php?error=1');
}

?>