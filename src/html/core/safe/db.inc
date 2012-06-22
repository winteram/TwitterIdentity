<?php

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