# Remove unneeded columns from the viral miRNA data for the viral-miRNA table
cut -f 1,2,5  ./data/vmt.tsv > ./data/vmt_cleaned.tsv
# Remove header line
tail -n 7283 ./data/vmt_cleaned.tsv > ./data/vmt_cleaned.tsv

# Remove unneed columns from the BioGRID data
cut -f 2,3,8,9 ./data/biogrid_9606_3.5.169.tsv > ./data/biogrid_9606_3.5.169_cleaned.tsv

# Get data for the viral-target table
cut -f 1,7  ./data/vmt.tsv > ./data/viral_target_data.tsv
# Remove header line
tail -n 7283 ./data/viral_target_data.tsv > ./data/viral_target_data.tsv

