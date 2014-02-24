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

echo "Twitter Connection Accounts:\n";
// Get all user names
$rqst = $dbh->prepare("SELECT Id, AccountName FROM twitterconnectionaccounts;");
$rqst->execute();

while($user_ca = $rqst->fetch(PDO::FETCH_ASSOC))
  {
    echo "ID: " . $user_ca['Id'] . " = " . decode_salt($user_ca['Id']) . "; Account Name: " . decode_salt($user_ca['AccountName']) . "\n";
  }

echo "\n";
echo "Survey Respondents:\n";
// Get all user names
$rqst = $dbh->prepare("SELECT survey.Id, AccountName FROM survey LEFT JOIN twitterconnectionaccounts tc ON survey.Id=tc.Id;");
$rqst->execute();

while($user_s = $rqst->fetch(PDO::FETCH_ASSOC))
  {
    echo "ID: " . $user_s['Id'] . " = " . decode_salt($user_s['Id']) . "; Account Name: " . decode_salt($user_s['AccountName']) . "\n";
  }


$mark = 0;
$seed = 1;
echo "\n";
echo "Seeds:\n";
// Get all user names
$rqst = $dbh->prepare("SELECT ta.Id, AccountName FROM twitteraccountnode ta LEFT JOIN twitterconnectionaccounts tc ON ta.Id=tc.Id WHERE Marked=:mark AND Seed=:seed;");
$rqst->bindParam(':mark',$mark, PDO::PARAM_INT);
$rqst->bindParam(':seed',$seed, PDO::PARAM_INT);
$rqst->execute();

while($user_seed = $rqst->fetch(PDO::FETCH_ASSOC))
  {
    echo "ID: " . $user_seed['Id'] . " = " . decode_salt($user_seed['Id']) . "; Account Name: " . decode_salt($user_seed['AccountName']) . "\n";
  }
