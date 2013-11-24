<?php 

$db_server = "localhost";
$db_username = "dbuser";
$db_password = "dbpassword";
$db_name = "dbname";

# Lets connect to the Database and set up the table
mysql_connect($db_server,$db_username,$db_password);
mysql_select_db($db_name);
$ct_res = mysql_query("CREATE TABLE IF NOT EXISTS `facebook_user` (
   `session_key` VARCHAR( 80 ) NOT NULL ,
   `uid` VARCHAR( 80 ) NOT NULL ,
   `expires` VARCHAR( 80 ) NOT NULL ,
   `secret` VARCHAR( 80 ) NOT NULL ,
   `access_token` VARCHAR( 120 ) NOT NULL ,
   `sig` VARCHAR( 80 ) NOT NULL
   );"
);


# Now lets load the FB GRAPH API
require '../src/facebook.php';

// Create our Application instance.
global $facebook;
$facebook = new Facebook(array(
 'appId'  => '101001010101010101',
 'secret' => 'faafaffdfasdffsafsfsddfasd',
 'cookie' => false,
));

# Lets set up the permissions we need and set the login url in case we need it.
$par['req_perms'] = "offline_access,
                    user_groups,
                    friends_groups,
                    user_interests,
                    friends_interests,
                    user_likes,
                    friends_likes,
                    user_religion_politics,
                    friends_religion_politics,
                    user_status,
                    friends_status,
                    read_stream";
$par['next'] = 'http://smallsocialsystems.com/groupid/FBAuth.php'
$loginUrl = $facebook->getLoginUrl($par);

function get_check_session(){
  global $facebook;
  # This function basically checks for a stored session and if we have one returns it,
  #If we have no stored session then it gets one and stores it
  # OK lets go to the database and see if we have a session stored
  $sid=mysql_query("Select access_token from facebook_user");
  $session_id=mysql_fetch_row($sid);
  if (is_array($session_id)) {
    # We have a session ID so lets not get a new one
    # Put some session checking in here to make sure its valid
   try {
     $attachment =  array('access_token' => $session_id[0],);
     $ret_code=$facebook->api('/me', 'GET', $attachment);
    }
     catch (Exception $e) {
       # We don't have a good session so
       echo "woops";
      $res = mysql_query('delete from facebook_user where expires=0');
      return;
    }
  return $session_id[0];
 } else {
  # Are we coming back from a login with a session set?
  $session = $facebook->getSession();
  if (is_array($session)) {
   # Yes! so lets store it!
   $sql="insert into facebook_user (
               session_key,
               uid,
               expires,
               secret,
               access_token,
               sig)
             VALUES ('".$session['session_key']."','".
                        $session['uid']."','".
                        $session['expires']."','".
                        $session['secret'] ."','".
                        $session['access_token']."','".
                        $session['sig']."');";
   $res = mysql_query($sql);
   return $session['access_token'];
  }
 }
}

$access_token=get_check_session();
# If we've not got an access_token we need to login.
if ( is_null($access_token) ) {
echo '<a href="'. $loginUrl.'"><
img src="http://static.ak.fbcdn.net/rsrc.php/zB6N8/hash/4li2k73z.gif" alt="" /> ';
}
else {

# This is where you put your code.

}

?>