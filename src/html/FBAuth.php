<?php 
session_start();
require_once('core/fb-php/src/facebook.php');
require_once('../safe/config.inc');
global $dbh;


$config = array(
      'appId' => APP_ID,
      'secret' => APP_SECRET,
      'fileUpload' => false, // optional
      'allowSignedRequest' => false, // optional, but should be set to false for non-canvas apps
  );

$facebook = new Facebook($config);
$fbid_raw = $facebook->getUser();

if($fbid_raw) {

  // We have a user ID, so probably a logged in user.
  // If not, we'll get an exception, which we handle below.
  try {
    $user = $facebook->api('/me','GET');
    if(!isset($_SESSION['fb_status']))
    { 
      // The user has been verified and the access tokens can be saved for future use 
      $_SESSION['fb_status'] = 'verified';
      $_SESSION['userid'] = $userid = isset($_SESSION['userid']) ? $_SESSION['userid'] : bin2hex(openssl_random_pseudo_bytes(16));
      // error_log("userid: ".$userid);

      $username = encode_salt($user['username']); 
      $fbid = encode_salt($fbid_raw); 
      // error_log("fbid: ".$fbid);

      // Check if survey exists for twitter id
      $rqst = $dbh->prepare("SELECT Id FROM users WHERE Id=:userid");
      $rqst->bindParam(':userid',$userid, PDO::PARAM_STR);
      $row = $rqst->execute();
      $result = $rqst->fetch(PDO::FETCH_ASSOC);
      if ($result['Id'] === $userid) {
        $query = "UPDATE users SET FBid=:fbid WHERE Id=:userid";
        $rqst2 = $dbh->prepare($query);
        $rqst2->bindParam(':fbid',$fbid, PDO::PARAM_STR);
        $rqst2->bindParam(':userid',$userid, PDO::PARAM_STR);
        $rqst2->execute();
      } else {
        // Add connection info
        $query = "INSERT INTO users SET Id=:userid, FBid=:fbid";
        $rqst2 = $dbh->prepare($query);
        $rqst2->bindParam(':userid',$userid, PDO::PARAM_STR);
        $rqst2->bindParam(':fbid',$fbid, PDO::PARAM_STR);
        $rqst2->execute();
      }

      $access_token = $facebook->getAccessToken();
      $app_access_token = $facebook->getApplicationAccessToken();
      $query = "INSERT INTO fbconnectionaccounts SET Id=:userid, 
                AccessToken=:token,
                AppAccessToken=:apptoken,
                CreationDate=NOW()";
      $rqst2 = $dbh->prepare($query);
      $rqst2->bindParam(':userid',$userid, PDO::PARAM_STR);
      $rqst2->bindParam(':token',encode_salt($access_token), PDO::PARAM_STR);
      $rqst2->bindParam(':apptoken',encode_salt($app_access_token), PDO::PARAM_STR);
      $rqst2->execute();

      // TODO: insert data from user's profile?

      if(isset($_SESSION['IU'])) {
        header('Location: ./IUConsent.php');
      } else {
        header('Location: ./Consent.php');
      }
    }
    else {
        echo "FBstatus already set.";
    }
  } catch(FacebookApiException $e) {
    if(isset($_SESSION['IU'])) {
      unset($_SESSION['fb_status']);
      header('Location: ./IUConsent.php?error=3');
    } else {
      unset($_SESSION['fb_status']);
      header('Location: ./Consent.php?error=3');
    }
    // echo "{'status':'error','message':'".$e->getMessage()."','type':'".$e->getType()."'}";
  }     
  
} else {
  if(isset($_SESSION['IU'])) {
    unset($_SESSION['fb_status']);
    header('Location: ./IUConsent.php?error=4');
  } else {
    unset($_SESSION['fb_status']);
    header('Location: ./Consent.php?error=4');
  }

}

?>