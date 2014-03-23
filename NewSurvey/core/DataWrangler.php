<?php

// Get data for accessing database
require_once('safe/config.inc');
global $dbh;
global $full_csw;
/*if(empty($full_csw))
{
$full_csw=array();
}
*/


global $traits_full = 
  ['capable', 'comfortable', 'communicative', 'confident', 'disagreeing', 'disorganized', 
  'energetic', 'friendly', 'fun and entertaining', 'giving', 'happy', 'hardworking', 'hopeless', 
  'immature', 'incompetent', 'indecisive', 'independent', 'inferior', 'insecure', 'intelligent', 
  'interested', 'irresponsible', 'irritable', 'isolated', 'lazy', 'like a failure', 'lovable', 
  'mature', 'needed', 'optimistic', 'organized', 'outgoing', 'sad and blue', 'self-centered', 
  'successful', 'tense', 'uncomfortable', 'unloved', 'weary', 'worthless'];


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
  $ownform11 = isset($freeform['ownform11']) ? $freeform['ownform11'] : "NULL";
  $ownform12 = isset($freeform['ownform12']) ? $freeform['ownform12'] : "NULL";
  $userURL1 = isset($freeform['ownURL1']) ? $freeform['ownURL1'] : "NULL";
  $ownform21 = isset($freeform['ownform21']) ? $freeform['ownform21'] : "NULL";
  $ownform22 = isset($freeform['ownform22']) ? $freeform['ownform22'] : "NULL";
  $userURL2 = isset($freeform['ownURL2']) ? $freeform['ownURL2'] : "NULL";
  $ownform31 = isset($freeform['ownform31']) ? $freeform['ownform31'] : "NULL";
  $ownform32 = isset($freeform['ownform32']) ? $freeform['ownform32'] : "NULL";
  $userURL3 = isset($freeform['ownURL3']) ? $freeform['ownURL3'] : "NULL";

  $rqst = $dbh->prepare("UPDATE survey SET own_form11=:ownform11, own_form12=:ownform12, own_URL1=:userURL1, 
    own_form21=:ownform21, own_form22=:ownform22, own_URL2=:userURL2, own_form31=:ownform31, own_form32=:ownform32, 
    own_URL3=:userURL3 WHERE Id=:twitid");
  $rqst->bindParam(':ownform11',$ownform11, PDO::PARAM_STR);
  $rqst->bindParam(':ownform12',$ownform12, PDO::PARAM_STR);
  $rqst->bindParam(':userURL1',$userURL1, PDO::PARAM_STR);
  $rqst->bindParam(':ownform21',$ownform21, PDO::PARAM_STR);
  $rqst->bindParam(':ownform22',$ownform22, PDO::PARAM_STR);
  $rqst->bindParam(':userURL2',$userURL2, PDO::PARAM_STR);
  $rqst->bindParam(':ownform31',$ownform31, PDO::PARAM_STR);
  $rqst->bindParam(':ownform32',$ownform32, PDO::PARAM_STR);
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
    $aspectid = $rqst->fetch(PDO::FETCH_ASSOC);
    if(isset($aspectid))
    {
      $rqst = $dbh->prepare("UPDATE aspects SET Label=:label WHERE Id=:aspectid");
      $rqst->bindParam(':label',$aspect_label, PDO::PARAM_INT);
      $rqst->bindParam(':aspectid',$aspectid['Id'], PDO::PARAM_INT);
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
    $aspectid = $rqst->fetch(PDO::FETCH_ASSOC);
    if(isset($aspectid))
    {
      $import = isset($asp_gen['import']) ? $asp_gen['import'] : -1;
      $pos = isset($asp_gen['pos']) ? $asp_gen['pos'] : -1;
      $rqst = $dbh->prepare("UPDATE aspects SET Positive=:pos, Important=:import WHERE Id=:aspectid");
      $rqst->bindParam(':pos',$pos, PDO::PARAM_INT);
      $rqst->bindParam(':import',$import, PDO::PARAM_INT);
      $rqst->bindParam(':aspectid',$aspectid['Id'], PDO::PARAM_INT);
      $rqst->execute();
    }
  }
  break;
case 'smqs': // social media questionnaire
  $smedia = $_REQUEST['media'];
  if($smedia != 'fb' && $smedia != 'tw') break;

  $smasps = $_REQUEST['sm_asp'];
  foreach($smasps as $name => $smq)
  {
    $rqst = $dbh->prepare("SELECT Id FROM aspects WHERE UserId=:twitid AND Name=:name");
    $rqst->bindParam(':twitid',$twitid, PDO::PARAM_STR);
    $rqst->bindParam(':name',$name, PDO::PARAM_STR);
    $row = $rqst->execute();
    $result = $rqst->fetch(PDO::FETCH_ASSOC);
    if(isset($result))
    {
      if($smedia=='fb')
      {
        $rqst = $dbh->prepare("UPDATE aspects SET Facebook=:smval WHERE Id=:aspectid");
        $rqst->bindParam(':smval',$smq, PDO::PARAM_INT);
        $rqst->bindParam(':aspectid',$aspectid['Id'], PDO::PARAM_INT);
        $rqst->execute();
      } 
      else if($smedia=='tw')
      {
        $rqst = $dbh->prepare("UPDATE aspects SET Twitter=:smval WHERE Id=:aspectid");
        $rqst->bindParam(':smval',$smq, PDO::PARAM_INT);
        $rqst->bindParam(':aspectid',$aspectid['Id'], PDO::PARAM_INT);
        $rqst->execute();
      }
    }
  }
  $smfbk = $_REQUEST['sm_fbk'];
  $smqs = $_REQUEST['sm_gen'];
  $smcomms = $_REQUEST['sm_com'];
  $smqnames = array('feel','doing','where','entertain','political','family','god','academic','appearance');
  $query = 'UPDATE survey SET ' . $smedia . '_comments=:sm_fbk, ';
  $ctr = 0;
  foreach($smqs as $i => $smq)
    {
      $query .= $smedia . "_" . $varnames[$i] . "=:" . $smedia . $ctr . ", ";
      $query .= $smedia . "_" . $varnames[$i] . "_comments=:" . $smedia . $ctr . "_comm, ";
      $ctr += 1;
    }
  $query = substr($query, 0, -2) . " WHERE Id=:twitid";
  //echo $query . "\n";
  $dbh->setAttribute(PDO::ATTR_EMULATE_PREPARES, false);  
  $rqst = $dbh->prepare($query);
  $rqst->bindParam(':sm_fbk', $smfbk, PDO::PARAM_STR);
  $ctr = 0;
  foreach($smqs as $i => $smq)
    {
      $rqst->bindParam(':' . $smedia . $ctr, intval($smq), PDO::PARAM_INT);
      $rqst->bindParam(':' . $smedia . $ctr."_comm", $smcomms[$i], PDO::PARAM_STR);
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




case 'csw_data': // This will take the 35 entries from the contingencies of self worth questions. 
  $sentnames=array(); /* debating whether I should use new meaningful names for each response, or just use the names
 from trial_newest */

  $cswq = $_REQUEST['data'];
  $query = 'UPDATE survey SET ';

  foreach($cswq as $key => $response)
  {
    $query .= $key . "=:". $key . ", ";
  }

  $query = substr($query, 0, -2) . " WHERE Id=:twitid";

  error_log(print_r($query,true));

  $dbh->setAttribute(PDO::ATTR_EMULATE_PREPARES, false); 
  $rqst = $dbh->prepare($query);
  foreach($cswq as $key => $response)
  {
    
    $rqst->bindParam(':' . $key, intval($response), PDO::PARAM_INT);

  
    error_log(print_r($cswq[$key],true));
    //error_log(print_r($response,true));
    
  }  
  $rqst->bindParam(':twitid',$twitid, PDO::PARAM_STR);
  $rqst->execute();

  break;


case 'panas':
  $panas = $_REQUEST['data'];
  error_log(print_r($panas,true));

  $query = 'UPDATE survey SET ';

  foreach($panas as $key => $response)
  {
    $query .= $key . "=:". $key . ", ";
  }

  $query = substr($query, 0, -2) . " WHERE Id=:twitid";

  error_log(print_r($query,true));

  $dbh->setAttribute(PDO::ATTR_EMULATE_PREPARES, false); 
  $rqst = $dbh->prepare($query);
  foreach($panas as $key => $response)
  {
    
    $rqst->bindParam(':' . $key, intval($response), PDO::PARAM_INT);

  
    error_log(print_r($panas[$key],true));
    //error_log(print_r($response,true));
    
  } 
  $rqst->bindParam(':twitid',$twitid, PDO::PARAM_STR);
  $rqst->execute();


  break;





  //$stage = $_REQUEST['stage'];

  //error_log(print_r($stage,true));

  /*if($stage==1)
  {
    //$cswq_1 = $cswq;
    global $cswq_full;
    $cswq_full=$cswq;

  }
  else
  {
    $cswq_full=$cswq_full+$cswq;
    error_log(print_r($cswq_full))
  } */
  

  /*if($stage==2)
  {
    $cswq_2 = $cswq;
  }
  if($stage==3)
  {
    $cswq_full = $cswq_1 + $cswq_2 + $cswq;
    error_log(print_r($cswq_full,true));
  }

  */





  
default:
  echo "ERR: invalid page";
}



?>