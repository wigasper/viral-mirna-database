# viral-mirna-final-project
Final project for my BIOI 4870 (Database Search & Pattern Discovery) class.

## File Descriptions
**format_gene_ontology.py** - Converts the gene ontology in OBO format into a tab delimited format  
**get_uniprot_ids.py** - Uses the UniProt API to retrieve and store XML files for a list of needed UniProt IDs specified by [Qureshi et al.'s viral miRNA target data](http://crdd.osdd.net/servers/virmirna/)  
**initialize_db.sql** - Postgre code to set up the database  
**prep_data.sh** - Shell script to remove unneeded columns and headers from raw data  
**uniprot_data_extraction.py** - Extracts required data for the database from UniProt XMLs  
