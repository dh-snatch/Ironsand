<?php

$url = "http://192.168.56.13:5000/insert_sample"; // backend VM endpoint

// Data from the form
$data = [
    "name" => $_POST['name'],
    "latitude" => floatval($_POST['latitude']),
    "longitude" => floatval($_POST['longitude']),
    "rock_type" => $_POST['rock_type'],
    "description" => $_POST['description'] ?? "",
    "date_discovered" => $_POST['date_discovered']
];

$options = [
    'http' => [
        'header'  => "Content-Type: application/json\r\n",
        'method'  => 'POST',
        'content' => json_encode($data),
    ],
];

$context  = stream_context_create($options);
$result = file_get_contents($url, false, $context);
// redirect back to the main page
header("Location: http://127.0.0.1:8080/");

?>
