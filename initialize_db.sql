/* Create tables */
CREATE TABLE viral_miRNA (
    vi_miRNA_id             varchar,        -- Unique viral miRNA ID
    virus                   varchar,        -- The virus associated with the viral miRNA
    miRNA_symbol            varchar         -- The miRNA symbol of the viral miRNA
);

CREATE TABLE viral_target (
    vi_miRNA_id             varchar,        -- Unique viral miRNA ID
    uniprot_id              varchar         -- Unique UniProt protein ID
);

CREATE TABLE protein (
    uniprot_id              varchar,        -- Unique UniProt protein ID
    symbol                  varchar,        -- Gene symbol
    full_name               varchar,        -- Full name of the gene
    gene_id                 int,            -- Entrez Gene ID for the gene
    tissue                  varchar         -- Tissue specificity for the gene
);

CREATE TABLE protein_interaction (
    interactor_a_gene_id    int,            -- Entrez Gene ID for interactor A
    interactor_b_gene_id    int,            -- Entrez Gene ID for interactor B
    interactor_a_symbol     varchar,        -- Gene symbol for interactor A
    interactor_b_symbol     varchar         -- Gene symbol for interactor B
);

CREATE TABLE annotates (
    uniprot_id              varchar,        -- Unique UniProt protein ID
    go_id                   varchar         -- Unique GO ID for the term applied to the gene

);

CREATE TABLE goterm (
    go_id                   varchar,        -- Unique GO ID for the term
    term                    varchar,        -- Natural language description of the term
    term_namespace          varchar         -- Term namespace
);

/* Copy over data */
\copy viral_miRNA FROM './data/viral_mirna_data.tsv' WITH NULL AS '-'
\copy viral_target FROM './data/viral_target_data.tsv' WITH NULL AS '-'
\copy protein FROM './data/proteins.tab' WITH NULL AS '-'
\copy protein_interaction FROM './data/protein_interaction_data.tsv' WITH NULL AS '-'
\copy annotates FROM './data/annotates.tab' WITH NULL AS '-'
\copy goterm FROM './data/go.tab' WITH NULL AS '-'
