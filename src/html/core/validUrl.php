<?php

$user_url = $_REQUEST['user_url'];

$ch = curl_init($user_url);
curl_setopt($ch, CURLOPT_NOBODY, true);
$output = curl_exec($ch);
curl_close($ch);

echo $output == 1 ? $output : 0;

?>

