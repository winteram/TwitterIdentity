<?php

// Get data for accessing database
require_once('safe/db.inc');
global $dbh;

$errmsg = "Missing data";

if (isset($_REQUEST['username']))
{
  $username = $_REQUEST['username'];
}
else 
{
  echo "ERR: username not set";
  exit(0);
}

// determine what data to be entered to db
$page = $_REQUEST['page'];

switch($page) 
{
case 'new':
  // put responses to consent form in dB
  $agree1 = isset($_REQUEST['agree']) ? intval($_REQUEST['agree']) : 0;
  $agree2 = isset($_REQUEST['agree2']) ? intval($_REQUEST['agree2']) : 0;

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
  break;
case 'demog':
  // parse data into array
  // print_r($_REQUEST['data']);
  $demogs = $_REQUEST['data'];

  // ensure valid values will be entered
  $gender = isset($demogs['gender']) ? $demogs['gender'] : "NULL";
  $yob = isset($demogs['age']) ? intval($demogs['age']) : "NULL";
  $country = isset($demogs['loc']) ? $demogs['loc'] : "NULL";
  $ethnicity = isset($demogs['races']) ? implode(",",$demogs['races']) : "NULL";
  $income = isset($demogs['income']) ? $demogs['income'] : "NULL";
  $edu = isset($demogs['edu']) ? $demogs['edu'] : "NULL";

  echo $gender . "\n";
  echo $yob . "\n";
  echo $country . "\n";
  echo $ethnicity . "\n";
  echo $income . "\n";
  echo $edu . "\n";
  echo $username;

  // prepare data to enter into db
  $rqst = $dbh->prepare("UPDATE survey SET gender=:gender, yob=:yob, country=:country, ethnicity=:ethnic, income=:income, edu=:edu WHERE username=:uname");
  $rqst->bindParam(':gender',$gender, PDO::PARAM_STR);
  $rqst->bindParam(':yob',$yob, PDO::PARAM_INT);
  $rqst->bindParam(':country',$country, PDO::PARAM_STR);
  $rqst->bindParam(':ethnic',$ethnicity, PDO::PARAM_STR);
  $rqst->bindParam(':income',$income, PDO::PARAM_INT);
  $rqst->bindParam(':edu',$edu, PDO::PARAM_STR);
  $rqst->bindParam(':uname',$username, PDO::PARAM_STR);
  $rqst->execute();
  break;

default:
  echo "ERR: invalid page";
}



?>