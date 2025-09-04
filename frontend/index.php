<?php

// backend VM endpoint
$url = "http://192.168.56.13:5000/deposits";

// json from backend/main.py
$json_data = file_get_contents($url);
$json_data = @file_get_contents($url);

if ($json_data === false) {
    die("Could not fetch deposits from backend.");
}

$deposits = json_decode($json_data, true);

if ($deposits === null) {
    die("JSON decode error: " . json_last_error_msg());
}
?>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ironsand</title>
</head>
<body>
    <h1>Ironsand</h1>
    <nav>
        <a href="index.html">Home</a>
        <a href="add_deposit.html">Add Deposit</a>
        <a href="view_deposit.html">View Deposit</a>
    </nav>
    <ul>
   <h1>Deposits</h1>
    <?php if (!empty($deposits)): ?>
        <ul>
            <?php foreach ($deposits as $deposit): ?>
                <li>
                    <strong>Name:</strong> <?php echo htmlspecialchars($deposit['name']); ?><br>
                    <strong>Rock Type:</strong> <?php echo htmlspecialchars($deposit['rock_type']); ?><br>
                    <strong>Description:</strong> <?php echo htmlspecialchars($deposit['description']); ?><br>
                    <strong>Location:</strong> <?php echo $deposit['latitude'] . ", " . $deposit['longitude']; ?><br>
                    <strong>Date Discovered:</strong> <?php echo $deposit['date_discovered']; ?>
                </li>
            <?php endforeach; ?>
        </ul>
    <?php endif; ?>
</ul>
    
</body>
</html>