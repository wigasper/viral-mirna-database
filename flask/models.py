# coding: utf-8
from sqlalchemy import Column, Integer, MetaData, String, Table

metadata = MetaData()


t_annotates = Table(
    'annotates', metadata,
    Column('uniprot_id', String),
    Column('go_id', String)
)


t_goterm = Table(
    'goterm', metadata,
    Column('go_id', String),
    Column('term', String),
    Column('term_namespace', String)
)


t_protein = Table(
    'protein', metadata,
    Column('uniprot_id', String),
    Column('symbol', String),
    Column('full_name', String),
    Column('gene_id', Integer),
    Column('tissue', String)
)


t_protein_interaction = Table(
    'protein_interaction', metadata,
    Column('interactor_a_gene_id', Integer),
    Column('interactor_b_gene_id', Integer),
    Column('interactor_a_symbol', String),
    Column('interactor_b_symbol', String)
)


t_viral_mirna = Table(
    'viral_mirna', metadata,
    Column('vi_mirna_id', String),
    Column('virus', String),
    Column('mirna_symbol', String)
)


t_viral_target = Table(
    'viral_target', metadata,
    Column('vi_mirna_id', String),
    Column('uniprot_id', String)
)
