<?php

// Get data for accessing database
require_once('safe/config.inc');
global $dbh;
global $traits_full = 
  ['capable', 'comfortable', 'communicative', 'confident', 'energetic', 
   'friendly', 'fun and entertaining', 'giving', 'happy', 'hardworking',
   'independent', 'intelligent', 'interested', 'lovable', 'mature', 'needed', 
   'optimistic', 'organized', 'outgoing', 'successful','disagreeing', 'disorganized', 
   'hopeless', 'immature', 'incompetent', 'indecisive', 'inferior', 'insecure', 'irresponsible', 'irritable', 
   'isolated', 'lazy', 'like a failure', 'sad and blue', 'self-centered', 
   'tense', 'uncomfortable', 'unloved', 'weary', 'worthless'];

$errmsg = "Missing data";

if (isset($_REQUEST['twitid']))
{
  $twitid = encode_salt($_REQUEST['twitid']);
}
else 
{
  echo "ERR: twitid not set";
  //exit(0);
}

// determine what data to be entered to db
$page = $_REQUEST['page'];

switch($page) 
{
case 'new':
case 'demog':
  // parse data into array
  echo $_REQUEST['data'];
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
case 'party': // answers to survey for political id
case 'nation': // answers to survey for national id
  $answers = $_REQUEST['data'];
  $varnames = array('bond','solidarity','committed','glad','proud','pleasant','goodfeel','think','identity',
    'seemyself','common_avg','similar_avg','common_oth','similar_oth');
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
      echo ':' . $page . $ctr . ' = ' . $response . '\n';
      $rqst->bindParam(':' . $page . $ctr, intval($answers[$key]), PDO::PARAM_INT);
      $ctr += 1;
    }  
  $rqst->bindParam(':twitid',$twitid, PDO::PARAM_STR);
  $rqst->execute();
  break;
case 'freeform':
  $freeform = $_REQUEST['data'];
  // print_r($freeform);
  // echo $freeform;
  $ownform1 = isset($freeform['ownform1']) ? $freeform['ownform1'] : "NULL";
  $ownform2 = isset($freeform['ownform2']) ? $freeform['ownform2'] : "NULL";
  $userURL = isset($freeform['ownURL']) ? $freeform['ownURL'] : "NULL";
  $ownform3 = isset($freeform['ownform3']) ? $freeform['ownform3'] : "NULL";
  $ownform4 = isset($freeform['ownform4']) ? $freeform['ownform4'] : "NULL";
  $userURL2 = isset($freeform['ownURL2']) ? $freeform['ownURL2'] : "NULL";
  $ownform5 = isset($freeform['ownform5']) ? $freeform['ownform5'] : "NULL";
  $ownform6 = isset($freeform['ownform6']) ? $freeform['ownform6'] : "NULL";
  $userURL3 = isset($freeform['ownURL3']) ? $freeform['ownURL3'] : "NULL";

  $rqst = $dbh->prepare("UPDATE survey SET own_form1=:ownform1, own_form2=:ownform2, own_URL=:userURL, 
    own_form3=:ownform3, own_form4=:ownform4, own_URL2=:userURL2, own_form5=:ownform5, own_form6=:ownform6, 
    own_URL3=:userURL3 WHERE Id=:twitid");
  $rqst->bindParam(':ownform1',$ownform1, PDO::PARAM_STR);
  $rqst->bindParam(':ownform2',$ownform2, PDO::PARAM_STR);
  $rqst->bindParam(':userURL',$userURL, PDO::PARAM_STR);
  $rqst->bindParam(':ownform3',$ownform3, PDO::PARAM_STR);
  $rqst->bindParam(':ownform4',$ownform4, PDO::PARAM_STR);
  $rqst->bindParam(':userURL2',$userURL2, PDO::PARAM_STR);
  $rqst->bindParam(':ownform5',$ownform5, PDO::PARAM_STR);
  $rqst->bindParam(':ownform6',$ownform6, PDO::PARAM_STR);
  $rqst->bindParam(':userURL3',$userURL3, PDO::PARAM_STR);
  $rqst->bindParam(':twitid',$twitid, PDO::PARAM_STR);
  $rqst->execute();
  break;
case 'aspects': // self aspects
  $aspects = $_REQUEST['data'];
  foreach($aspects as $key => $aspect)
  {
    $name = isset($aspect["name"]) ? $aspect["name"] : "NULL";
    $rqst = $dbh->prepare("INSERT INTO aspects SET UserId=:twitid, Name=:name");
    $rqst->bindParam(':twitid',$twitid, PDO::PARAM_STR);
    $rqst->bindParam(':name',$name, PDO::PARAM_STR);
    $rqst->execute();
    $aspectid = $dbh->lastInsertId();
    if(isset($aspect["traits"]))
    {
      foreach($aspect["traits"] as $key=>$trait)
      {
        $traitid = array_search($trait, $traits_full);
        $rqst = $dbh->prepare("INSERT INTO aspects_traits SET AspectId=:aspectid, TraitId=:traitid");
        $rqst->bindParam(':aspectid',$aspectid, PDO::PARAM_INT);
        $rqst->bindParam(':traitid',$traitid, PDO::PARAM_INT);
        $rqst->execute();
      }
    }
  }
  break;
case 'aspect_labs': // 
  $aspect_labs = $_REQUEST['data'];
  foreach($aspect_labs as $name => $aspect_label)
  {
    $rqst = $dbh->prepare("SELECT Id FROM aspects WHERE UserId=:twitid AND Name=:name");
    $rqst->bindParam(':twitid',$twitid, PDO::PARAM_STR);
    $rqst->bindParam(':name',$name, PDO::PARAM_STR);
    $row = $rqst->execute();
    $result = $rqst->fetch(PDO::FETCH_ASSOC);
    if(isset($result))
    {
      $rqst = $dbh->prepare("UPDATE aspects SET Label=:label WHERE Id=:aspectid");
      $rqst->bindParam(':label',$aspect_label, PDO::PARAM_INT);
      $rqst->bindParam(':aspectid',$aspectid, PDO::PARAM_INT);
      $rqst->execute();
    }
  }
  break;
case 'selfqs': // self aspects questionnaire
  $selfqs = $_REQUEST['data'];
  foreach($selfqs as $name => $asp_gen)
  {
    $rqst = $dbh->prepare("SELECT Id FROM aspects WHERE UserId=:twitid AND Name=:name");
    $rqst->bindParam(':twitid',$twitid, PDO::PARAM_STR);
    $rqst->bindParam(':name',$name, PDO::PARAM_STR);
    $row = $rqst->execute();
    $result = $rqst->fetch(PDO::FETCH_ASSOC);
    if(isset($result))
    {
      $import = isset($asp_gen['import']) ? $asp_gen['import'] : -1;
      $pos = isset($asp_gen['pos']) ? $asp_gen['pos'] : -1;
      $rqst = $dbh->prepare("UPDATE aspects SET Positive=:pos, Important=:import WHERE Id=:aspectid");
      $rqst->bindParam(':pos',$pos, PDO::PARAM_INT);
      $rqst->bindParam(':import',$import, PDO::PARAM_INT);
      $rqst->bindParam(':aspectid',$aspectid, PDO::PARAM_INT);
      $rqst->execute();
    }
  }
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
  if ($result['Id'] === $twitid) {
    $rqst = $dbh->prepare("UPDATE twitteraccountnode SET Marked=:mark, Seed=:seed WHERE Id=:twitid");
    $rqst->bindParam(':mark',$mark, PDO::PARAM_INT);
    $rqst->bindParam(':seed',$seed, PDO::PARAM_INT);
    $rqst->bindParam(':twitid',$twitid, PDO::PARAM_STR);
    $rqst->execute();    
  } elseif ($twitid != ''){
    // Add user to be crawled
    $rqst = $dbh->prepare("INSERT INTO twitteraccountnode SET Id=:twitid, Marked=:mark, CreationDate=NOW(), Seed=:seed");
    $rqst->bindParam(':twitid',$twitid, PDO::PARAM_STR);
    $rqst->bindParam(':mark',$mark, PDO::PARAM_INT);
    $rqst->bindParam(':seed',$seed, PDO::PARAM_INT);
    $rqst->execute();
  } else {
    echo "ERR: bad id: " .$twitid;
  }

  break;
default:
  echo "ERR: invalid page";
}



?>