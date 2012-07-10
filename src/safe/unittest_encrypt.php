<?php
require_once('config.inc'); 

function randString($length, $charset='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_')
{
  $str = '';
  $count = strlen($charset);
  while ($length--) {
    $str .= $charset[mt_rand(0, $count-1)];
  }
  return $str;
}

$noerr = TRUE;

for ($i=0;$i<50;$i++)
  {
    $string = randString($i+1);
    $key = randString(6);
    if($string != decode_salt(encode_salt($string)))
      {
	print $string . ", " . encode_salt($string) . ", " . decode_salt(encode_salt($string));
	$noerr = FALSE;
      }
  }

if ($noerr)
  {
    print "Success!";
  }

?>