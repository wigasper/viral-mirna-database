#!/usr/bin/env python3

# This script is used to extract data needed for my database
# from previously downloaded UniProt XML files.

import pandas as pd
from tqdm import tqdm
from bs4 import BeautifulSoup

viruses = ["EBV", "KSHV"]
uniprot_ids = []

# Get IDs to extract info for:
with open("./data/vmt.tsv", "r") as handle:
    for line in handle:
        line = line.split("\t")
        if line[1] in viruses: 
            uniprot_ids.append(line[6])

# Remove duplicates
uniprot_ids = list(dict.fromkeys(uniprot_ids))

# FileNotFoundErrors:
fnfe = []

# Other errors:
errors = []

# prot_data list order:
# [UniProt ID, Symbol, Full Name, GeneID, GO IDs, Tissues]
prot_data = []

for ID in tqdm(uniprot_ids):
    try:
        with open("./UniProt XMLs/{}.xml".format(ID), "r") as handle:
            prot = [ID]
            symbol = "-"
            full_name = "-"
            gene_id = "-"
            go_ids = []
            tissues = []
            
            soup = BeautifulSoup(handle.read())
            # Get symbol
            if soup.gene is not None:
                for name in soup.gene.find_all("name"):
                    if name['type'] == "primary":
                        symbol = name.text
            prot.append(symbol)
            # Get full name
            full_name = soup.find("fullname").text
            prot.append(full_name)
            # Get GO IDs and GeneID
            for ref in soup.find_all("dbreference"):
                if ref['type'] == "GO":
                    go_ids.append(ref['id'])
                if ref['type'] == "GeneID":
                    gene_id = ref['id']
            prot.append(gene_id)
            prot.append(go_ids)
            # Get tissue specificity if available:
            for tissue in soup.find_all("tissue"):
                tissues.append(tissue.text)
            prot.append(tissues)
            
            # Add to prot_data list
            prot_data.append(prot)
    except FileNotFoundError:
        fnfe.append(ID)
    except AttributeError:
        errors.append(ID)

# Save as tab delim
with open("./data/proteins_raw.tab", "w") as out:
    for prot in prot_data:
        out.write(prot[0])
        out.write("\t")
        out.write(prot[1])
        out.write("\t")
        out.write(prot[2])
        out.write("\t")
        out.write(prot[3])
        out.write("\t")
        out.write(", ".join(prot[4]))
        out.write("\t")
        out.write(", ".join(prot[5]))
        out.write("\n")

# Save as CSV
prot_df = pd.DataFrame(prot_data, columns=['UniProtID', 'Symbol', 'FullName', 
                                           'GeneID', 'GOIDs', 'Tissues'])
prot_df.to_csv("./data/proteins.csv")

# FNFEs belong to IDs that generated unresolvable errors on the pull
# due to being obsolete. Recording for future reference
with open("./data/fnfes_from_uniprot_mining.csv", "w") as f:
    for e in fnfe:
        f.write(e)
        f.write("\n")

# After examination, the IDs that raised AttributeErrors are
# deprecated, deleted, or otherwise obsolete. Recording these for
# future reference
with open("./data/obsolete_or_deleted_UniProtIDs.csv", "w") as f:
    for e in errors:
        f.write(e)
        f.write("\n")

# Annotation data will be stored separately in the DB
# Initialize list to store annotation data
annotate_table_data = []

# Extract annotation data
for prot in prot_data:
    for go_term in prot[4]:
        entry = [prot[0], go_term]
        annotate_table_data.append(entry)

# Save as tab delim
with open("./data/annotates.tab", "w") as out:
    for annotation in annotate_table_data:
        out.write(annotation[0])
        out.write("\t")
        out.write(annotation[1])
        out.write("\n")