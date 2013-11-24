<?php

// Get data for accessing database
require_once('../../safe/config.inc');
global $dbh;

$errmsg = "Missing data";

if (isset($_REQUEST['userid']))
{
  $userid = encode_salt($_REQUEST['userid']);
}
else 
{
  echo "ERR: userid not set";
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
  $rqst = $dbh->prepare("UPDATE survey SET gender=:gender, yob=:yob, country=:country, ethnicity=:ethnic, income=:income, edu=:edu WHERE Id=:userid");
  $rqst->bindParam(':gender',$gender, PDO::PARAM_STR);
  $rqst->bindParam(':yob',$yob, PDO::PARAM_INT);
  $rqst->bindParam(':country',$country, PDO::PARAM_STR);
  $rqst->bindParam(':ethnic',$ethnicity, PDO::PARAM_STR);
  $rqst->bindParam(':income',$income, PDO::PARAM_INT);
  $rqst->bindParam(':edu',$edu, PDO::PARAM_STR);
  $rqst->bindParam(':userid',$userid, PDO::PARAM_STR);
  $rqst->execute();
  break;
case 'polform': // party affiliation
  $party = isset($_REQUEST['party']) ? $_REQUEST['party'] : "NULL";
  $rqst = $dbh->prepare("UPDATE survey SET party=:party WHERE Id=:userid");
  $rqst->bindParam(':party',$party, PDO::PARAM_STR);
  $rqst->bindParam(':userid',$userid, PDO::PARAM_STR);
  $rqst->execute();
  break;
case 'natform':
  $nationality = isset($_REQUEST['nationality']) ? $_REQUEST['nationality'] : "NULL";
  $rqst = $dbh->prepare("UPDATE survey SET nationality=:nationality WHERE Id=:userid");
  $rqst->bindParam(':nationality',$nationality, PDO::PARAM_STR);
  $rqst->bindParam(':userid',$userid, PDO::PARAM_STR);
  $rqst->execute();
  break;
case 'freeform':
  $freeform = $_REQUEST['data'];
  //print_r($freeform);
  $ownform1 = isset($freeform['ownform1']) ? $freeform['ownform1'] : "NULL";
  $ownform2 = isset($freeform['ownform2']) ? $freeform['ownform2'] : "NULL";
  $userURL = isset($freeform['ownURL']) ? $freeform['ownURL'] : "NULL";
  $ownform3 = isset($freeform['ownform3']) ? $freeform['ownform3'] : "NULL";
  $ownform4 = isset($freeform['ownform4']) ? $freeform['ownform4'] : "NULL";
  $userURL2 = isset($freeform['ownURL2']) ? $freeform['ownURL2'] : "NULL";
  $ownform5 = isset($freeform['ownform5']) ? $freeform['ownform5'] : "NULL";
  $ownform6 = isset($freeform['ownform6']) ? $freeform['ownform6'] : "NULL";
  $userURL3 = isset($freeform['ownURL3']) ? $freeform['ownURL3'] : "NULL";

  $rqst = $dbh->prepare("UPDATE survey SET own_form1=:ownform1, own_form2=:ownform2, own_URL=:userURL, own_form3=:ownform3, own_form4=:ownform4, own_URL2=:userURL2, own_form5=:ownform5, own_form6=:ownform6, own_URL3=:userURL3 WHERE Id=:userid");
  $rqst->bindParam(':ownform1',$ownform1, PDO::PARAM_STR);
  $rqst->bindParam(':ownform2',$ownform2, PDO::PARAM_STR);
  $rqst->bindParam(':userURL',$userURL, PDO::PARAM_STR);
  $rqst->bindParam(':ownform3',$ownform3, PDO::PARAM_STR);
  $rqst->bindParam(':ownform4',$ownform4, PDO::PARAM_STR);
  $rqst->bindParam(':userURL2',$userURL2, PDO::PARAM_STR);
  $rqst->bindParam(':ownform5',$ownform5, PDO::PARAM_STR);
  $rqst->bindParam(':ownform6',$ownform6, PDO::PARAM_STR);
  $rqst->bindParam(':userURL3',$userURL3, PDO::PARAM_STR);
  $rqst->bindParam(':userid',$userid, PDO::PARAM_STR);
  $rqst->execute();
  break;
case 'party': // answers to survey for political id
case 'nation': // answers to survey for national id
  $answers = $_REQUEST['data'];
  $varnames = array('bond','solidarity','committed','glad','proud','pleasant','goodfeel','think','identity','seemyself','common_avg','similar_avg','common_oth','similar_oth');
  $query = 'UPDATE survey SET ';
  $ctr = 1;
  foreach($answers as $x)
    {
      $query .= $page . $ctr . "_" . $varnames[$ctr-1] . "=:" . $page . $ctr . ", ";
      $ctr += 1;
    }
  $query = substr($query, 0, -2) . " WHERE Id=:userid";
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
  $rqst->bindParam(':userid',$userid, PDO::PARAM_STR);
  $rqst->execute();
  break;
case 'comments': // comments on survey
  // Insert comments
  $comments = $_REQUEST['comments'];
  $comments = isset($_REQUEST['comments']) ? $_REQUEST['comments'] : "NULL";

  $rqst = $dbh->prepare("UPDATE survey SET comments=:comments WHERE Id=:userid");
  $rqst->bindParam(':comments',$comments, PDO::PARAM_STR);
  $rqst->bindParam(':userid',$userid, PDO::PARAM_STR);
  $rqst->execute();

  // Check if accountnode exists for twitter id
  $rqst = $dbh->prepare("SELECT Id, Marked, Seed FROM twitteraccountnode WHERE Id=:userid");
  $rqst->bindParam(':userid',$userid, PDO::PARAM_STR);
  $row = $rqst->execute();
  $result = $rqst->fetch(PDO::FETCH_ASSOC);

  $mark = 0;
  $seed = 1;
  if ($result['Id'] === $userid) {
    $rqst = $dbh->prepare("UPDATE twitteraccountnode SET Marked=:mark, Seed=:seed WHERE Id=:userid");
    $rqst->bindParam(':mark',$mark, PDO::PARAM_INT);
    $rqst->bindParam(':seed',$seed, PDO::PARAM_INT);
    $rqst->bindParam(':userid',$userid, PDO::PARAM_STR);
    $rqst->execute();    
  } elseif ($userid != ''){
    // Add user to be crawled
    $rqst = $dbh->prepare("INSERT INTO twitteraccountnode SET Id=:userid, Marked=:mark, CreationDate=NOW(), Seed=:seed");
    $rqst->bindParam(':userid',$userid, PDO::PARAM_STR);
    $rqst->bindParam(':mark',$mark, PDO::PARAM_INT);
    $rqst->bindParam(':seed',$seed, PDO::PARAM_INT);
    $rqst->execute();
  } else {
    echo "ERR: bad id: " .$userid;
  }

  break;
default:
  echo "ERR: invalid page";
}



?>