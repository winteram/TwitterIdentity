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

// Check if survey exists for username
$rqst = $dbh->prepare("SELECT username FROM survey WHERE username=:uname");
$rqst->bindParam(':uname',$username, PDO::PARAM_STR);
$user = $rqst->execute();

// if username exists, it will match (= error)
$new = ($user == $username) ? 'error' : 'new';

// put responses to consent form in dB
$agree1 = isset($_REQUEST['agree']) ? intval($_REQUEST['agree']) : 0;
$agree2 = isset($_REQUEST['agree2']) ? intval($_REQUEST['agree2']) : 0;

// determine what data to be entered to db
$page = isset($_REQUEST['page']) ? $_REQUEST['page'] : $new;

switch($page) 
{
case 'new':
  $rqst = $dbh->prepare("INSERT INTO survey SET username=:uname, agree1=:agree1, agree2=:agree2");
  $rqst->bindParam(':uname',$username, PDO::PARAM_STR);
  $rqst->bindParam(':agree1',$agree1, PDO::PARAM_INT);
  $rqst->bindParam(':agree2',$agree2, PDO::PARAM_INT);
  $rqst->execute();
  break;
case 'demographics':
  // parse data into array
  $demogs = parse_json($_REQUEST['data']);

  // ensure valid values will be entered
  $gender = isset($demogs['gender']) ? $demogs['gender'] : "NULL";
  $yob = isset($demogs['yob']) ? $demogs['yob'] : "NULL";
  $country = isset($demogs['country']) ? $demogs['country'] : "NULL";
  $ethnicity = isset($demogs['ethnicity']) ? $demogs['ethnicity'] : "NULL";
  $income = isset($demogs['income']) ? $demogs['income'] : "NULL";
  $edu = isset($demogs['edu']) ? $demogs['edu'] : "NULL";

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

case 'error':
  $errmsg = "Username exists in database";
default:
  echo "ERR: " . $errmsg;
}



?>