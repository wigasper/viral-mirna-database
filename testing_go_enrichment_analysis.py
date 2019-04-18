#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 18:31:00 2019

@author: wkg
"""

from goatools.base import download_ncbi_associations
gene2go = download_ncbi_associations()

from goatools.obo_parser import GODag

obodag = GODag("go.obo")



from __future__ import print_function
from goatools.associations import read_ncbi_gene2go

geneid2gos = read_ncbi_gene2go("gene2go", taxids=[9606])

from goatools.test_data.genes_NCBI_9606_ProteinCoding import GENEID2NT as gene_id_2_nt



from goatools.go_enrichment import GOEnrichmentStudy

goeaobj = GOEnrichmentStudy(
        gene_id_2_nt.keys(), # List of mouse protein-coding genes
        geneid2gos, # geneid/GO associations
        obodag, # Ontologies
        propagate_counts = False,
        alpha = 0.05, # default significance cut-off
        methods = ['fdr_bh']) # defult multipletest correction method

gene