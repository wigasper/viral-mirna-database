# Remove unneeded columns from the viral miRNA data for the viral-miRNA table
# and remove header line
cut -f 1,2,5  ./data/vmt.tsv | tail -n 7283 | grep 'EBV\|KSHV' > ./data/viral_mirna_data.tsv

# Remove unneed columns from the BioGRID data and remove header
cut -f 2,3,8,9 ./data/biogrid_raw.tsv | tail -n 468058 > ./data/protein_interaction_data.tsv

# Get data for the viral-target table and remove header line
cut -f 1,7  ./data/vmt.tsv | tail -n 7283 > ./data/viral_target_data.tsv

# Remove GO terms from protein data, these will only be needed in the 
# Annotates table
cut -f 1,2,3,4,6 ./data/proteins_raw.tab > ./data/proteins.tab