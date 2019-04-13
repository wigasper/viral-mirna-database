from app import db

class annotates(db.Model):
    __table__ = 'annotates'

    uniprot_id = db.Column(db.String(10), primary_key=True)
    go_id = db.Column(db.String(20), primary_key=True)

class goterm(db.Model):
    __table__ = 'goterm'

    go_id = db.Column(db.String(20), primary_key=True)
    term = db.Column(db.String(80))
    term_namespace = db.Column(String(80))

class protein(db.Model):
    __table__ = 'protein'

    uniprot_id = db.Column(db.String(10), primary_key=True)
    symbol = db.Column(db.String(12))
    full_name = db.Column(db.String(30))
    gene_id = db.Column(db.Integer)
    tissue = db.Column(db.String(80))

class protein_interaction(db.Model):
    __table__ = 'protein_interaction'

    interactor_a_gene_id = db.Column(db.Integer, primary_key=True)
    interactor_b_gene_id = db.Column(db.Integer, primary_key=True)
    interactor_a_symbol = db.Column(db.String(12))
    interactor_b_symbol = db.Column(db.String(12))

class viral_mirna(db.Model):
    __table__ = 'viral_mirna'

    vi_mirna_id = db.Column(db.String(15), primary_key=True)
    virus = db.column(db.String(12))
    mirna_symbol = db.column(db.String(20))

class viral_target(db.Model):
    __table__ = 'viral_target'

    vi_mirna_id = db.Column(db.String(15), primary_key=True)
    uniprot_id = db.Column(db.String(10))