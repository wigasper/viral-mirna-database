\copy (SELECT protein.symbol, protein_interaction.interactor_b_symbol FROM protein, protein_interaction, viral_target, viral_mirna WHERE viral_mirna.virus = 'EBV' AND viral_mirna.vi_mirna_id = viral_target.vi_mirna_id AND viral_target.uniprot_id = protein.uniprot_id AND protein.symbol = protein_interaction.interactor_a_symbol ORDER BY protein.symbol ASC) to '/media/wkg/storage/db-final-project/ebv_target_interactions.csv' with csv

\copy (SELECT protein.symbol, protein_interaction.interactor_b_symbol FROM protein, protein_interaction, viral_target, viral_mirna WHERE viral_mirna.virus = 'KSHV' AND viral_mirna.vi_mirna_id = viral_target.vi_mirna_id AND viral_target.uniprot_id = protein.uniprot_id AND protein.symbol = protein_interaction.interactor_a_symbol ORDER BY protein.symbol ASC) to '/media/wkg/storage/db-final-project/kshv_target_interactions.csv' with csv

SELECT protein.symbol, protein_interaction.interactor_b_symbol, viral_mirna.virus 
FROM protein, protein_interaction, viral_target, viral_mirna 
WHERE viral_mirna.virus = 'EBV'
AND viral_mirna.vi_mirna_id = viral_target.vi_mirna_id
AND viral_target.uniprot_id = protein.uniprot_id
AND protein.symbol = protein_interaction.interactor_a_symbol 
ORDER BY protein.symbol ASC;

SELECT protein.symbol, protein_interaction.interactor_b_symbol, viral_mirna.virus 
FROM protein, protein_interaction, viral_target, viral_mirna 
WHERE viral_mirna.virus = 'KSHV'
AND viral_mirna.vi_mirna_id = viral_target.vi_mirna_id
AND viral_target.uniprot_id = protein.uniprot_id
AND protein.symbol = protein_interaction.interactor_a_symbol 
ORDER BY protein.symbol ASC;