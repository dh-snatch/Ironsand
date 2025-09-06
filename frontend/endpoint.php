<?php

// backend VM endpoint
$url = "http://192.168.56.13:5000/retrieve_samples";


// json from backend/main.py
$json_data = @file_get_contents($url);


if ($json_data === false) {
    die("Could not fetch deposits from backend.");
}

$samples = json_decode($json_data, true);

if ($samples === null) {
    die("JSON decode error: " . json_last_error_msg());
}

header('Content-Type: application/json');
echo json_encode($samples);
?>
