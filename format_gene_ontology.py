import os

import pandas as pd

os.chdir("/media/wkg/storage/db-final-project")

# A list to store GO terms
go_terms = []

# A single term
term = []

# Open the ontology text file and parse
with open("./data/go.obo", "r") as go:
    for line in go:
        if line.startswith("[Term]"):
            if term:
                go_terms.append(term)
            term = []
        if line.startswith("id: "):
            term.append(line[4:].strip("\n"))
        if line.startswith("name: "):
            term.append(line[6:].strip("\n"))
        if line.startswith("namespace: "):
            term.append(line[11:].strip("\n"))

# Append final term
go_terms.append(term)

# Write as a tab-delimited file for insertion into the DB
with open("go.tab", "w") as out:
    for term in go_terms:
        out.write(term[0])
        out.write("\t")
        out.write(term[1])
        out.write("\t")
        out.write(term[2])
        out.write("\n")