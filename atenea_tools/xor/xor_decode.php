<?php
$message = "XORprocedure";
$password = "awesomepassword";

$decoded_message = '';
for ($i = 0; $i < strlen($message); $i++) {
    $decoded_message .= chr(ord($message[$i]) ^ ord($password[$i % strlen($password)]));
}

echo $decoded_message;
?>
