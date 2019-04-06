/* Create tables */
\i /media/wkg/storage/db-final-project/create_tables.sql

/* Copy over data */
\copy viral_miRNA FROM '/media/wkg/storage/db-final-project/data/viral_mirna_data.tsv' WITH NULL AS '-'
\copy viral_target FROM '/media/wkg/storage/db-final-project/data/viral_target_data.tsv' WITH NULL AS '-'
\copy protein FROM '/media/wkg/storage/db-final-project/data/proteins.tab' WITH NULL AS '-'
\copy protein_interaction FROM '/media/wkg/storage/db-final-project/data/protein_interaction_data.tsv' WITH NULL AS '-'
\copy annotates FROM '/media/wkg/storage/db-final-project/data/annotates.tab' WITH NULL AS '-'
\copy goterm FROM '/media/wkg/storage/db-final-project/data/go.tab' WITH NULL AS '-'