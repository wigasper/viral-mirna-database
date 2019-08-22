#!/usr/bin/env python3
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="The Gene Ontology in OBO format",
            required=True, type=str)
    args = parser.parse_args()

    # A list to store GO terms
    go_terms = []

    # A single term
    term = []

    # Open the ontology text file and parse
    with open(args.input, "r") as go:
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
    with open("./data/go.tab", "w") as out:
        for term in go_terms:
            out.write("\t".join([term[0], term[1], term[2]]))
            out.write("\n")
