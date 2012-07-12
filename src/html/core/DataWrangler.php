<?php

// Get data for accessing database
require_once('../../safe/config.inc');
global $dbh;

$errmsg = "Missing data";

if (isset($_REQUEST['twitid']))
{
  $twitid = encode_salt($_REQUEST['twitid']);
}
else 
{
  echo "ERR: twitid not set";
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
  $rqst = $dbh->prepare("UPDATE survey SET gender=:gender, yob=:yob, country=:country, ethnicity=:ethnic, income=:income, edu=:edu WHERE Id=:twitid");
  $rqst->bindParam(':gender',$gender, PDO::PARAM_STR);
  $rqst->bindParam(':yob',$yob, PDO::PARAM_INT);
  $rqst->bindParam(':country',$country, PDO::PARAM_STR);
  $rqst->bindParam(':ethnic',$ethnicity, PDO::PARAM_STR);
  $rqst->bindParam(':income',$income, PDO::PARAM_INT);
  $rqst->bindParam(':edu',$edu, PDO::PARAM_STR);
  $rqst->bindParam(':twitid',$twitid, PDO::PARAM_STR);
  $rqst->execute();
  break;
case 'polform': // party affiliation
  $party = isset($_REQUEST['party']) ? $_REQUEST['party'] : "NULL";
  $rqst = $dbh->prepare("UPDATE survey SET party=:party WHERE Id=:twitid");
  $rqst->bindParam(':party',$party, PDO::PARAM_STR);
  $rqst->bindParam(':twitid',$twitid, PDO::PARAM_STR);
  $rqst->execute();
  break;
case 'natform':
  $nationality = isset($_REQUEST['nationality']) ? $_REQUEST['nationality'] : "NULL";
  $rqst = $dbh->prepare("UPDATE survey SET nationality=:nationality WHERE Id=:twitid");
  $rqst->bindParam(':nationality',$nationality, PDO::PARAM_STR);
  $rqst->bindParam(':twitid',$twitid, PDO::PARAM_STR);
  $rqst->execute();
  break;
case 'freeform':
  $freeform = $_REQUEST['data'];
  //print_r($freeform);
  $ownform1 = isset($freeform['ownform1']) ? $freeform['ownform1'] : "NULL";
  $ownform2 = isset($freeform['ownform2']) ? $freeform['ownform2'] : "NULL";
  $userURL = isset($freeform['ownURL']) ? $freeform['ownURL'] : "NULL";

  $rqst = $dbh->prepare("UPDATE survey SET own_form1=:ownform1, own_form2=:ownform2, own_URL=:userURL WHERE Id=:twitid");
  $rqst->bindParam(':ownform1',$ownform1, PDO::PARAM_STR);
  $rqst->bindParam(':ownform2',$ownform2, PDO::PARAM_STR);
  $rqst->bindParam(':userURL',$userURL, PDO::PARAM_STR);
  $rqst->bindParam(':twitid',$twitid, PDO::PARAM_STR);
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
  $query = substr($query, 0, -2) . " WHERE Id=:twitid";
  //echo $query . "\n";
  $dbh->setAttribute(PDO::ATTR_EMULATE_PREPARES, false);  
  $rqst = $dbh->prepare($query);
  $ctr = 1;
  foreach($answers as $key => $response)
    {
      //echo ':' . $page . $ctr . ' = ' . $response . '\n';
      $rqst->bindParam(':' . $page . $ctr, intval($answers[$key]), PDO::PARAM_INT);
      $ctr += 1;
    }  
  $rqst->bindParam(':twitid',$twitid, PDO::PARAM_STR);
  $rqst->execute();
  break;
case 'comments': // comments on survey
  // Insert comments
  $comments = $_REQUEST['comments'];
  $comments = isset($_REQUEST['comments']) ? $_REQUEST['comments'] : "NULL";

  $rqst = $dbh->prepare("UPDATE survey SET comments=:comments WHERE Id=:twitid");
  $rqst->bindParam(':comments',$comments, PDO::PARAM_STR);
  $rqst->bindParam(':twitid',$twitid, PDO::PARAM_STR);
  $rqst->execute();

  // Check if accountnode exists for twitter id
  $rqst = $dbh->prepare("SELECT Id, Marked, Seed FROM twitteraccountnode WHERE Id=:twitid");
  $rqst->bindParam(':twitid',$twitid, PDO::PARAM_STR);
  $row = $rqst->execute();
  $result = $rqst->fetch(PDO::FETCH_ASSOC);

  $mark = 0;
  $seed = 1;
  if ($result['twitid'] === $twitid) {
    $rqst = $dbh->prepare("UPDATE twitteraccountnode SET Marked=:mark, Seed=:seed WHERE Id=:twitid");
    $rqst->bindParam(':mark',$mark, PDO::PARAM_INT);
    $rqst->bindParam(':seed',$seed, PDO::PARAM_INT);
    $rqst->bindParam(':twitid',$twitid, PDO::PARAM_STR);
    $rqst->execute();    
  } else {
    // Add user to be crawled
    $rqst = $dbh->prepare("INSERT INTO twitteraccountnode SET Id=:twitid, Marked=:mark, CreationDate=NOW(), Seed=:seed");
    $rqst->bindParam(':twitid',$twitid, PDO::PARAM_STR);
    $rqst->bindParam(':mark',$mark, PDO::PARAM_INT);
    $rqst->bindParam(':seed',$seed, PDO::PARAM_INT);
    $rqst->execute();
  }

  break;
default:
  echo "ERR: invalid page";
}



?>