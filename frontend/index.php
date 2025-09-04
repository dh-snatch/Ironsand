<?php
$servername = "192.168.56.12"; 
$username = "webuser";
$password = "placeholder_password";
$dbname = "ironsand";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
echo "Connection established successfully";


// Query the deposits table
$sql = "SELECT name, rock_type, latitude, longitude, description FROM DEPOSIT";
$result = $conn->query($sql);
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
        <?php
            if ($result->num_rows > 0) {
                while($row = $result->fetch_assoc()) {
                    echo "<li><b>".$row['name']."</b> (".$row['rock_type'].") - ".$row['description']."</li>";
                }
            } else {
                echo "<li>No deposits found.</li>";
            }
            $conn->close();
        ?>
</ul>
    
</body>
</html>