<?php

$id = $_GET['id'] ?? null;
// backend VM endpoint
$url = "http://192.168.56.13:5000/delete_sample?id=$id";

$data = file_get_contents("php://input");

echo($data);
$options = [
    'http' => [
        'method' => 'DELETE',
    ],
];


$context  = stream_context_create($options);
$result = file_get_contents($url, false, $context);

?>

