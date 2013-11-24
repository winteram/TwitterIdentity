<?php

// Access keys for Twitter oAuth
define('CONSUMER_KEY', 'zhew9FPCoQGPRnR4PHPB3A');
define('CONSUMER_SECRET', 'ToHQwjgWSX4v3NUsRxe7IthQ6TUmTT78bJKcDIey7LY');
define('OAUTH_CALLBACK', 'http://smallsocialsystems.com/asaf/Landing.php');

// Access keys for Facebook oAuth
define('APP_ID', '230481670452212');
define('APP_SECRET', 'ba78c45a8092200ab63ef73fbd76d67e');

// Database config
$host = "localhost";
$user = "groupid";
$pass = "letspublish";
$db   = "gidb";


try {
  $dbh = new PDO('mysql:host='.$host.';dbname='.$db, $user, $pass);
} catch (PDOException $e) {
  print "Error!: " . $e->getMessage() . "<br/>";
  die();
}


function encode_salt($sData, $sKey='xJp2BpRUSE'){ 
  $sResult = ''; 
  for($i=0;$i<strlen($sData);$i++){ 
    $sChar    = substr($sData, $i, 1); 
    $sKeyChar = substr($sKey, ($i % strlen($sKey)) - 1, 1); 
    $sChar    = chr(ord($sChar) + ord($sKeyChar)); 
    $sResult .= $sChar; 
  } 
  return encode_base64($sResult); 
} 

function decode_salt($sData, $sKey='xJp2BpRUSE'){ 
  $sResult = ''; 
  $sData   = decode_base64($sData); 
  for($i=0;$i<strlen($sData);$i++){ 
    $sChar    = substr($sData, $i, 1); 
    $sKeyChar = substr($sKey, ($i % strlen($sKey)) - 1, 1); 
    $sChar    = chr(ord($sChar) - ord($sKeyChar)); 
    $sResult .= $sChar; 
  } 
  return $sResult; 
} 

function encode_base64($sData){
  $sBase64 = base64_encode($sData);
  return rtrim(strtr($sBase64, '+/', '-_'),'=');
}

function decode_base64($sData){
  $sBase64 = strtr($sData, '-_', '+/');
  return base64_decode($sBase64);
}

?>