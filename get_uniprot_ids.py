#!/usr/bin/env python3

import os
import requests
import time
from pathlib import Path

from tqdm import tqdm

os.chdir("/Users/wigasper/Documents/Classes/BIOI 4870/db-final-project")

viruses = ["EBV", "KSHV"]
uniprot_ids = []

with open("vmt.tsv", "r") as handle:
    for line in handle:
        line = line.split("\t")
        if line[1] in viruses: 
            uniprot_ids.append(line[6])

uniprot_ids = uniprot_ids[1:]

errors = []

for ID in tqdm(uniprot_ids):
    start_time = time.perf_counter()
    file = Path("./UniProt XMLs/{}.xml".format(ID))
    
    if not file.exists():
        req = requests.get("https://www.uniprot.org/uniprot/{}.xml".format(ID))
        if req.status_code != 200:
            errors.append([ID, req.status_code])
        else:
            with open(file, "w") as file_out:
                file_out.write(req.text)

    if time.perf_counter() - start_time < .1:
        time.sleep(.1 - (time.perf_counter() - start_time))