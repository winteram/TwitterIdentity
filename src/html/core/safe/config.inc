<?php

// Access keys for Twitter oAuth
define('CONSUMER_KEY', 'zhew9FPCoQGPRnR4PHPB3A');
define('CONSUMER_SECRET', 'ToHQwjgWSX4v3NUsRxe7IthQ6TUmTT78bJKcDIey7LY');
define('OAUTH_CALLBACK', 'http://smallsocialsystems.com/asaf/IdentitySurvey.php');

// Database config
$host = "localhost";
$user = "smalls7_groupid";
$pass = "letspublish";
$db   = "smalls7_identity";

try {
  $dbh = new PDO('mysql:host='.$host.';dbname='.$db, $user, $pass);
} catch (PDOException $e) {
  print "Error!: " . $e->getMessage() . "<br/>";
  die();
}


?>