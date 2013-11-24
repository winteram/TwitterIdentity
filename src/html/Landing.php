<?php 
session_start();
require_once('core/twitteroauth/twitteroauth.php');
require_once('../safe/config.inc');
global $dbh;
 
// If the oauth_token is old redirect to the connect page. 
if (isset($_REQUEST['oauth_token']) && $_SESSION['oauth_token'] !== $_REQUEST['oauth_token']) {
  $_SESSION['oauth_status'] = 'oldtoken';
  if(isset($_SESSION['IU'])) {
    unset($_SESSION['tw_status']);
    unset($_SESSION['oauth_token']);
    unset($_SESSION['oauth_token_secret']);
    header('Location: ./IUConsent.php?error=1');
  } else {
    unset($_SESSION['tw_status']);
    unset($_SESSION['oauth_token']);
    unset($_SESSION['oauth_token_secret']);
    header('Location: ./Consent.php?error=1');
  }
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
  $_SESSION['tw_status'] = 'verified';
  $connection = new TwitterOAuth(CONSUMER_KEY, CONSUMER_SECRET, $access_token['oauth_token'], $access_token['oauth_token_secret']);
  $user = $connection->get('account/verify_credentials');

  // Create userid and store in session variable if not exists
  $_SESSION['userid'] = $userid = isset($_SESSION['userid']) ? $_SESSION['userid'] : bin2hex(openssl_random_pseudo_bytes(16));
  $username = encode_salt($user->screen_name);
  $twitid = encode_salt($user->id);
  $oauth_token = encode_salt($access_token['oauth_token']);
  $oauth_secret = encode_salt($access_token['oauth_token_secret']);

  // Check if survey exists for twitter id
  $rqst = $dbh->prepare("SELECT Id FROM users WHERE Id=:userid");
  $rqst->bindParam(':userid',$userid, PDO::PARAM_STR);
  $row = $rqst->execute();
  $result = $rqst->fetch(PDO::FETCH_ASSOC);

  // if User ID exists, it will match
  if ($result['Id'] === $userid) {
    $query = "UPDATE users SET Twitid=:twitid WHERE Id=:userid";
    $rqst2 = $dbh->prepare($query);
    $rqst2->bindParam(':twitid',$twitid, PDO::PARAM_STR);
    $rqst2->bindParam(':userid',$userid, PDO::PARAM_STR);
    $rqst2->execute();
  } 
  else {
    // Add connection info
    $query = "INSERT INTO users SET Id=:userid, Twitid=:twitid";
    $rqst2 = $dbh->prepare($query);
    $rqst2->bindParam(':userid',$userid, PDO::PARAM_STR);
    $rqst2->bindParam(':twitid',$twitid, PDO::PARAM_STR);
    $rqst2->execute();

  }

  $query = "INSERT INTO twitterconnectionaccounts SET Id=:userid, AccessToken=:token, AccessTokenSecret=:secret, CreationDate=NOW()";
  $rqst2 = $dbh->prepare($query);
  $rqst2->bindParam(':userid',$userid, PDO::PARAM_STR);
  $rqst2->bindParam(':token',$oauth_token, PDO::PARAM_STR);
  $rqst2->bindParam(':secret',$oauth_secret, PDO::PARAM_STR);
  $rqst2->execute();
    /*
    $verified = $user->verified==1 ? 1 : 0;
    $geo = $user->geo_enabled==1 ? 1 : 0;
    $created_at = date("Y-m-d H:i:s",strtotime($user->created_at));
    //echo $created_at . ", " . strlen($username) . ", " . strlen(encode_salt($user->name));

    // Add profile information
    $query = "INSERT INTO tw_profile (Id, Name, Screen_name, Location, Created_at, Favourites_count, Url, Followers_count, Lang, Verified, Profile_bgd_color, Geo_enabled, Description, Time_zone, Friends_count, Statuses_count) VALUES (:userid, :uname, :screenname, :location, :created_at, :fav_cnt, :url, :fol_cnt, :lang, :verified, :profile_bgd, :geo, :descrip, :tz, :frnd_cnt, :twt_cnt)";
    $rqst2 = $dbh->prepare($query);
    $rqst2->bindParam(':userid',$userid, PDO::PARAM_STR);
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
    */

  // Send them to the survey
  if(isset($_SESSION['IU'])) {
    header('Location: ./IUConsent.php');
  } else {
    header('Location: ./Consent.php');
  }
} else {
  // Save HTTP status for error dialog on connnect page.
  if(isset($_SESSION['IU'])) {
    unset($_SESSION['tw_status']);
    unset($_SESSION['oauth_token']);
    unset($_SESSION['oauth_token_secret']);
    header('Location: ./IUConsent.php?error=2');
  } else {
    unset($_SESSION['tw_status']);
    unset($_SESSION['oauth_token']);
    unset($_SESSION['oauth_token_secret']);
    header('Location: ./Consent.php?error=2');
  }
}

?>