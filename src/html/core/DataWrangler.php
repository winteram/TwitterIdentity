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
case 'polform': // party affiliation
  $party = isset($_REQUEST['party']) ? $_REQUEST['party'] : "NULL";
  $rqst = $dbh->prepare("UPDATE survey SET party=:party WHERE username=:uname");
  $rqst->bindParam(':party',$party, PDO::PARAM_STR);
  $rqst->bindParam(':uname',$username, PDO::PARAM_STR);
  $rqst->execute();
  break;
case 'natform':
  $nationality = isset($_REQUEST['nationality']) ? $_REQUEST['nationality'] : "NULL";
  $rqst = $dbh->prepare("UPDATE survey SET nationality=:nationality WHERE username=:uname");
  $rqst->bindParam(':nationality',$nationality, PDO::PARAM_STR);
  $rqst->bindParam(':uname',$username, PDO::PARAM_STR);
  $rqst->execute();
  break;
case 'freeform':
  $freeform = $_REQUEST['data'];
  print_r($freeform);
  $ownform1 = isset($freeform['ownform1']) ? $freeform['ownform1'] : "NULL";
  $ownform2 = isset($freeform['ownform2']) ? $freeform['ownform2'] : "NULL";
  $userURL = isset($freeform['ownURL']) ? $freeform['ownURL'] : "NULL";

  $rqst = $dbh->prepare("UPDATE survey SET own_form1=:ownform1, own_form2=:ownform2, own_URL=:userURL WHERE username=:uname");
  $rqst->bindParam(':ownform1',$ownform1, PDO::PARAM_STR);
  $rqst->bindParam(':ownform2',$ownform2, PDO::PARAM_STR);
  $rqst->bindParam(':userURL',$userURL, PDO::PARAM_STR);
  $rqst->bindParam(':uname',$username, PDO::PARAM_STR);
  $rqst->execute();
  break;
case 'party': // answers to survey for political id
case 'nation': // answers to survey for national id
case 'own': // answers to survey for free-form id
  $answers = $_REQUEST['data'];
  $varnames = array('bond','solidarity','committed','glad','proud','pleasant','goodfeel','think','identity','seemyself','common_avg','similar_avg','common_oth','similar_oth');
  $query = 'UPDATE survey SET ';
  $ctr = 1;
  foreach($answers as $x)
    {
      $query .= $page . $ctr . "_" . $varnames[$ctr-1] . "=:" . $page . $ctr . ", ";
      $ctr += 1;
    }
  $query = substr($query, 0, -2) . " WHERE username=:uname";
  echo $query . "\n";
  $dbh->setAttribute(PDO::ATTR_EMULATE_PREPARES, false);  
  $rqst = $dbh->prepare($query);
  $ctr = 1;
  foreach($answers as $key => $response)
    {
      echo ':' . $page . $ctr . ' = ' . $response . '\n';
      $rqst->bindParam(':' . $page . $ctr, intval($answers[$key]), PDO::PARAM_INT);
      $ctr += 1;
    }  
  $rqst->bindParam(':uname',$username, PDO::PARAM_STR);
  $rqst->execute();
  $rqst->debugDumpParams();
  break;
default:
  echo "ERR: invalid page";
}



?>