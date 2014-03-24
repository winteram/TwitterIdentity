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
    $user = $facebook->api('/me ','GET');
    // error_log(print_r($user, true));
    // The user has been verified and the access tokens can be saved for future use 
    $_SESSION['fb_status'] = 'verified';
    $_SESSION['userid'] = $userid = isset($_SESSION['userid']) ? $_SESSION['userid'] : bin2hex(openssl_random_pseudo_bytes(16));
    error_log("userid: ".$userid);

    // error_log($user['username']);
    $username = encode_salt($user['username']); 
    $fbid = encode_salt($fbid_raw); 

    // Check if survey exists for user id
    $rqst = $dbh->prepare("SELECT Id FROM users WHERE Id=:userid");
    $rqst->bindParam(':userid',$userid, PDO::PARAM_STR);
    $row = $rqst->execute();
    $result = $rqst->fetch(PDO::FETCH_ASSOC);
    if ($result['Id'] === $userid) {
      $qp1 = "UPDATE ";
      $qp2 = " SET ";
      $qp3 = " WHERE Id=:userid";
    } else {
      $qp1 = "INSERT INTO ";
      $qp2 = " SET Id=:userid, ";
      $qp3 = "";
    }

    // Add connection info
    $query = $qp1."users".$qp2;
    $query .= "FBid=:fbid".$qp3;
    $rqst2 = $dbh->prepare($query);
    $rqst2->bindParam(':userid',$userid, PDO::PARAM_STR);
    $rqst2->bindParam(':fbid',$fbid, PDO::PARAM_STR);
    $rqst2->execute();

    $access_token = $facebook->getAccessToken();
    $app_access_token = $facebook->getApplicationAccessToken();
    // error_log('AccessToken: '.$access_token);
    // error_log('AppAccessToken: '.$app_access_token);
    $query = $qp1."fbconnectionaccounts".$qp2; 
    $query .= "AccessToken=:token,
              AppAccessToken=:apptoken,
              CreationDate=NOW()".$qp3;
    $rqst = $dbh->prepare($query);
    $rqst->bindParam(':userid',$userid, PDO::PARAM_STR);
    $rqst->bindParam(':token',encode_salt($access_token), PDO::PARAM_STR);
    $rqst->bindParam(':apptoken',encode_salt($app_access_token), PDO::PARAM_STR);
    $rqst->execute();

    $query = $qp1."fb_profile".$qp2; 
    $query .= "fbid=:fbid, username=:username";
    if (array_key_exists('name', $user)) $query .= ", name=:name";
    if (array_key_exists('birthday', $user)) $query .=  ", birthday=:birthday";
    if (array_key_exists('about', $user)) $query .=  ", about=:about";
    if (array_key_exists('bio', $user)) $query .= ", bio=:bio";
    if (array_key_exists('locale', $user)) $query .=  ", locale=:locale";
    if (array_key_exists('political', $user)) $query .=  ", political=:political";
    if (array_key_exists('website', $user)) $query .=  ", website=:website";
    if (array_key_exists('relationship_status', $user)) $query .=  ", relationship_status=:relationship_status";
    if (array_key_exists('religion', $user)) $query .=  ", religion=:religion";
    if (array_key_exists('gender', $user)) $query .=  ", sex=:sex";
    $query .= $qp3;
    error_log($query);

    $rqst = $dbh->prepare($query);
    $rqst->bindParam(':userid',$userid, PDO::PARAM_STR);
    $rqst->bindParam(':fbid',$fbid, PDO::PARAM_STR);
    $rqst->bindParam(':username',$username, PDO::PARAM_STR);
    if (array_key_exists('name', $user)) $rqst->bindParam(':name',encode_salt($user['name']), PDO::PARAM_STR);
    if (array_key_exists('birthday', $user)) $rqst->bindParam(':birthday',date('Y/m/d', strtotime($user['birthday'])), PDO::PARAM_STR);
    if (array_key_exists('about', $user)) $rqst->bindParam(':about',encode_salt($user['about']), PDO::PARAM_STR);
    if (array_key_exists('bio', $user)) $rqst->bindParam(':bio',encode_salt($user['bio']), PDO::PARAM_STR);
    if (array_key_exists('locale', $user)) $rqst->bindParam(':locale',$user['locale'], PDO::PARAM_STR);
    if (array_key_exists('political', $user)) $rqst->bindParam(':political',$user['political'], PDO::PARAM_STR);
    if (array_key_exists('website', $user)) $rqst->bindParam(':website',encode_salt($user['website']), PDO::PARAM_STR);
    if (array_key_exists('relationship_status', $user)) $rqst->bindParam(':relationship_status',$user['relationship_status'], PDO::PARAM_STR);
    if (array_key_exists('religion', $user)) $rqst->bindParam(':religion',$user['religion'], PDO::PARAM_STR);
    if (array_key_exists('gender', $user)) $rqst->bindParam(':sex',$user['gender'], PDO::PARAM_STR);
    $rqst->execute();

    if(isset($_SESSION['IU'])) {
      header('Location: ./IUConsent.php');
    } else {
      header('Location: ./Consent.php');
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