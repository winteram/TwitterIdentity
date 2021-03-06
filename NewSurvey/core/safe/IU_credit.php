<?php

require_once('config.inc');

// Database config
$host = "smallsocialsystems.com";
$user = "smalls7_groupid";
$pass = "letspublish";
$db   = "smalls7_identity";


try {
  $dbh = new PDO('mysql:host='.$host.';dbname='.$db, $user, $pass);
} catch (PDOException $e) {
  print "Error!: " . $e->getMessage() . "<br/>";
  die();
}


echo "Valid IU Participants\n";
// Get all user names
$query = "SELECT survey.Id, AccountName, IUname, Created_at, Followers_count, Statuses_count, own_form1 FROM ";
$query .=  "survey LEFT JOIN twitterconnectionaccounts tc ON survey.Id=tc.Id ";
$query .=  "LEFT JOIN profile ON survey.Id=profile.Id ";
$query .=  "WHERE IUname != '' AND IUname != 'NULL' ORDER BY survey.ended;";
//echo $query . "\n";
$rqst = $dbh->prepare($query);
$rqst->execute();

$valid_names = array();

while($user_s = $rqst->fetch(PDO::FETCH_ASSOC))
  {
    $response = "ID: " . $user_s['Id'];
    $response .= ", " . decode_salt($user_s['AccountName']) . "\n";
    $response .= "(" . $user_s['IUname']. ")\n";
    $response .= "\t Self-group: " . $user_s['own_form1']. "\n";
    $response .= "\t Created: " . $user_s['Created_at']. "\n";
    $response .= "\t Followers: " . $user_s['Followers_count']. "\n";
    $response .= "\t Tweets: " . $user_s['Statuses_count']. "\n\n";
    echo $response;
    $valid_names[] = $user_s['IUname'];
  }

//sort($valid_names);
foreach($valid_names as $name)
  {
    echo $name . "\n";
  }
echo "    (" . count($valid_names) . ")\n";