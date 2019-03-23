import os
from pathlib import Path

import pandas as pd
from tqdm import tqdm
from bs4 import BeautifulSoup

os.chdir("/media/wkg/storage/db-final-project")

viruses = ["EBV", "KSHV"]
uniprot_ids = []

# Get IDs to extract info for:
with open("vmt.tsv", "r") as handle:
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
# [UniProt ID, Symbol, Full Name, GO IDs, Tissues]
prot_data = []

for ID in tqdm(uniprot_ids):
    try:
        with open("./UniProt XMLs/{}.xml".format(ID), "r") as handle:
            prot = [ID]
            soup = BeautifulSoup(handle.read())
            # Get symbol
            if soup.gene is not None:
                for name in soup.gene.find_all("name"):
                    if name['type'] == "primary":
                        prot.append(name.text)
            else:
                prot.append("NA")
            # Get full name
            prot.append(soup.find("fullname").text)
            # Get GO IDs
            go_ids = []
            for ref in soup.find_all("dbreference"):
                if ref['type']== "GO":
                    go_ids.append(ref['id'])
            prot.append(go_ids)
            # Get tissue specificity if available:
            tissues = []
            for tissue in soup.find_all("tissue"):
                tissues.append(tissue.text)
            prot.append(tissues)
            
            # Add to prot_data list
            prot_data.append(prot)
    except FileNotFoundError:
        fnfe.append(ID)
    except AttributeError:
        errors.append(ID)

# Save
prot_data = pd.DataFrame(prot_data, columns=['UniProtID', 'Symbol', 'FullName', 'GOIDs', 'Tissues'])
prot_data.to_csv("proteins.csv")

# FNFEs belong to IDs that generated unresolvable errors on the pull
# due to being obsolete. Recording for future reference
with open("fnfes_from_uniprot_mining.csv", "w") as f:
    for e in fnfe:
        f.write(e)
        f.write("\n")

# After examination, the IDs that raised AttributeErrors are
# deprecated, deleted, or otherwise obsolete. Recording these for
# future reference
with open("obsolete_or_deleted_UniProtIDs.csv", "w") as f:
    for e in errors:
        f.write(e)
        f.write("\n")