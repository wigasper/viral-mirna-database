<html>
<head>
<title>My First PHP Page</title>
</head>
<body>
<form name="display" action="index.php" method="POST" >
<li>Protein Symbol:</li><li><input type="text" name="prot_symbol" /></li>
<li><input type="submit" name="submit" /></li>
</form>
<?php

$conn = pg_connect("host=localhost port=5432 dbname=vir_mirna user=wkg password=apples");

/*******Connection Status Check********/
if (!$conn) {
    die('Could not connect: ' . pg_error());
}
echo 'Connected successfully';
/***********************************/

$query = "SELECT DISTINCT vi_mirna_id FROM viral_mirna WHERE virus = '$_POST[prot_symbol]'";
$result = pg_query($query);
while ($row = pg_fetch_array($result))
{
    echo "Virus :{$row['vi_mirna_id']}<br>";
}
pg_close($conn); //close the connection
?>
</body>
</html>
