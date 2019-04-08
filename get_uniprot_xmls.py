#!/usr/bin/env python3
import os
import requests
import time
from pathlib import Path

from tqdm import tqdm

os.chdir("/Users/wigasper/Documents/Classes/BIOI 4870/db-final-project")
# os.chdir ("/media/wkg/storage/db-final-project")

# Viruses that I am concerned with for this database
viruses = ["EBV", "KSHV"]

# Empty list for UniProt IDs to get
uniprot_ids = []

# Get UniProt IDs from virMiRNA data
with open("vmt.tsv", "r") as handle:
    for line in handle:
        line = line.split("\t")
        if line[1] in viruses: 
            uniprot_ids.append(line[6])

# Drop header
uniprot_ids = uniprot_ids[1:]

# list for errors
errors = []

for ID in tqdm(uniprot_ids):
    start_time = time.perf_counter()
    file = Path("./UniProt XMLs/{}.xml".format(ID))
    
    # Check to see if file already exists, if not save the XML resulting
    # from the API call
    if not file.exists():
        req = requests.get("https://www.uniprot.org/uniprot/{}.xml".format(ID))
        if req.status_code != 200:
            # append to errors if there is an error code
            errors.append([ID, req.status_code])
        else:
            with open(file, "w") as file_out:
                file_out.write(req.text)

    # Sleep to avoid bogging down UniProt's server if making more than
    # 10 calls/second
    if time.perf_counter() - start_time < .1:
        time.sleep(.1 - (time.perf_counter() - start_time))