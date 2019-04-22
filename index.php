<!-- /var/www/html -->
<html>
<head>
<title>Viral miRNA Target Database</title>
<h1><center>Viral miRNA Target Database</center></h1>
<p><center>Welcome to the simplified user interface for the viral miRNA target database.</p>
</head>
<body>
<form name="display" action="index.php" method="POST" >
Please enter a gene symbol to get started:<br><input type="text" name="prot_symbol" /><br>
<input type="submit" name="submit" />
</form></center>
<?php

// Connect
$conn = pg_connect("host=localhost port=5432 dbname=vir_mirna user=wkg password=apples");

/*******Connection Status Check********/
if (!$conn) {
    die('Could not connect: ' . pg_error());
}
echo  '<center>Connected successfully</center><br><br>';
/***********************************/

// Get symbol
$symbol = $_POST[prot_symbol];


// Query
$query = "SELECT DISTINCT protein.symbol, protein.full_name, protein.tissue 
          FROM protein 
          WHERE protein.symbol = '".$symbol."'";

// Result
$result = pg_query($query);

// Display results if they exist
if (strlen($symbol) > 0) {
echo '<center>Search results:</center><br><br>';

// Display basic gene data
echo "<center><table border='1'><col width='110'><col width='250'><col width='600'>";
echo "<tr><td>Gene Symbol</td><td>Full Name</td><td>Tissue Specificity</td>";
while ($row = pg_fetch_array($result)){
    $symbol = $row['symbol'];
    $full_name = $row['full_name'];
    $tissue = $row['tissue'];
    echo "<tr><td>".$symbol."</td><td>".$full_name."</td><td>".$tissue."</td></tr>";
}
echo "</table></center>";

// Query for viral miRNA data
$query = "SELECT DISTINCT viral_mirna.virus 
          FROM viral_target, protein, viral_mirna 
          WHERE protein.symbol = '".$symbol."' 
          AND protein.uniprot_id = viral_target.uniprot_id
          AND viral_target.vi_mirna_id = viral_mirna.vi_mirna_id";

$result = pg_query($query);

// Display viral mirna data
echo "<br><br><center><b>".$symbol." is targeted by the following viruses:</b><br><br><table border='1'>";
while ($row = pg_fetch_array($result)){
    $virus = $row['virus'];
    echo "<tr><td>".$virus."</td></tr>";
}
echo "</table></center>";

$query = "SELECT DISTINCT viral_target.vi_mirna_id 
          FROM viral_target, protein, viral_mirna 
          WHERE protein.symbol = '".$symbol."' 
          AND protein.uniprot_id = viral_target.uniprot_id
          AND viral_target.vi_mirna_id = viral_mirna.vi_mirna_id";

$result = pg_query($query);

echo "<br><br><center><b>With the following viral miRNA IDs:<br><br></b><table border='1'>";
while ($row = pg_fetch_array($result)){
    $vi_mirna_id = $row['vi_mirna_id'];
    echo "<tr><td>".$vi_mirna_id."</td></tr>";
}
echo "</table></center>";

// Query for GO terms
$query = "SELECT DISTINCT goterm.term 
          FROM protein, annotates, goterm 
          WHERE protein.symbol = '".$symbol."' 
          AND protein.uniprot_id = annotates.uniprot_id 
          AND annotates.go_id = goterm.go_id";

$result = pg_query($query);

// Display GO terms
echo "<br><br><center><b>".$symbol." has been annotated with the following Gene Ontology 
        terms:<br><br></b><table border='1'>";
while ($row = pg_fetch_array($result)){
    $term = $row['term'];
    echo "<tr><td>".$term."</td></tr>";
}
echo "</table></center>";

}


pg_close($conn); //close the connection
?>
</body>
</html>
