# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class FoldseekArabidopsis(models.Model):
    uniprot_id = models.CharField(db_column='Uniprot_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    query = models.CharField(max_length=50, blank=True, null=True)
    target = models.CharField(max_length=50, blank=True, null=True)
    fident = models.FloatField(blank=True, null=True)
    alnlen = models.IntegerField(blank=True, null=True)
    mismatch = models.IntegerField(blank=True, null=True)
    gapopen = models.IntegerField(blank=True, null=True)
    qstart = models.IntegerField(blank=True, null=True)
    qend = models.IntegerField(blank=True, null=True)
    tstart = models.IntegerField(blank=True, null=True)
    tend = models.IntegerField(blank=True, null=True)
    evalue = models.FloatField(blank=True, null=True)
    bits = models.IntegerField(blank=True, null=True)
    alntmscore = models.FloatField(blank=True, null=True)
    qtmscore = models.FloatField(blank=True, null=True)
    ttmscore = models.FloatField(blank=True, null=True)
    lddt = models.FloatField(blank=True, null=True)
    prob = models.FloatField(blank=True, null=True)
    pocket_id = models.CharField(db_column='Pocket_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=50, blank=True, null=True)  # Field name made lowercase.
    protein_names = models.CharField(db_column='Protein_names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    gene_names = models.CharField(db_column='Gene_names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    organism = models.CharField(db_column='Organism', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subcellular = models.CharField(db_column='Subcellular', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    doi_id = models.CharField(db_column='DOI_ID', max_length=4096, blank=True, null=True)  # Field name made lowercase.
    pdb = models.CharField(db_column='PDB', max_length=256, blank=True, null=True)  # Field name made lowercase.
    string = models.CharField(db_column='STRING', max_length=50, blank=True, null=True)  # Field name made lowercase.
    function_cc = models.CharField(db_column='Function_CC', max_length=8192, blank=True, null=True)  # Field name made lowercase.
    bindingdb = models.CharField(db_column='BindingDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orthodb = models.CharField(db_column='OrthoDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    expressionatlas = models.CharField(db_column='ExpressionAtlas', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Foldseek_arabidopsis'


class FoldseekMaize(models.Model):
    uniprot_id = models.CharField(db_column='Uniprot_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    query = models.CharField(max_length=50, blank=True, null=True)
    target = models.CharField(max_length=50, blank=True, null=True)
    fident = models.FloatField(blank=True, null=True)
    alnlen = models.IntegerField(blank=True, null=True)
    mismatch = models.IntegerField(blank=True, null=True)
    gapopen = models.IntegerField(blank=True, null=True)
    qstart = models.IntegerField(blank=True, null=True)
    qend = models.IntegerField(blank=True, null=True)
    tstart = models.IntegerField(blank=True, null=True)
    tend = models.IntegerField(blank=True, null=True)
    evalue = models.FloatField(blank=True, null=True)
    bits = models.IntegerField(blank=True, null=True)
    alntmscore = models.FloatField(blank=True, null=True)
    qtmscore = models.FloatField(blank=True, null=True)
    ttmscore = models.FloatField(blank=True, null=True)
    lddt = models.FloatField(blank=True, null=True)
    prob = models.FloatField(blank=True, null=True)
    pocket_id = models.CharField(db_column='Pocket_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=50, blank=True, null=True)  # Field name made lowercase.
    protein_names = models.CharField(db_column='Protein_names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    gene_names = models.CharField(db_column='Gene_names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    organism = models.CharField(db_column='Organism', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subcellular = models.CharField(db_column='Subcellular', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    doi_id = models.CharField(db_column='DOI_ID', max_length=4096, blank=True, null=True)  # Field name made lowercase.
    pdb = models.CharField(db_column='PDB', max_length=256, blank=True, null=True)  # Field name made lowercase.
    string = models.CharField(db_column='STRING', max_length=50, blank=True, null=True)  # Field name made lowercase.
    function_cc = models.CharField(db_column='Function_CC', max_length=8192, blank=True, null=True)  # Field name made lowercase.
    bindingdb = models.CharField(db_column='BindingDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orthodb = models.CharField(db_column='OrthoDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    expressionatlas = models.CharField(db_column='ExpressionAtlas', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Foldseek_maize'


class FoldseekRice(models.Model):
    uniprot_id = models.CharField(db_column='Uniprot_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    query = models.CharField(max_length=50, blank=True, null=True)
    target = models.CharField(max_length=50, blank=True, null=True)
    fident = models.FloatField(blank=True, null=True)
    alnlen = models.IntegerField(blank=True, null=True)
    mismatch = models.IntegerField(blank=True, null=True)
    gapopen = models.IntegerField(blank=True, null=True)
    qstart = models.IntegerField(blank=True, null=True)
    qend = models.IntegerField(blank=True, null=True)
    tstart = models.IntegerField(blank=True, null=True)
    tend = models.IntegerField(blank=True, null=True)
    evalue = models.FloatField(blank=True, null=True)
    bits = models.IntegerField(blank=True, null=True)
    alntmscore = models.FloatField(blank=True, null=True)
    qtmscore = models.FloatField(blank=True, null=True)
    ttmscore = models.FloatField(blank=True, null=True)
    lddt = models.FloatField(blank=True, null=True)
    prob = models.FloatField(blank=True, null=True)
    pocket_id = models.CharField(db_column='Pocket_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=50, blank=True, null=True)  # Field name made lowercase.
    protein_names = models.CharField(db_column='Protein_names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    gene_names = models.CharField(db_column='Gene_names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    organism = models.CharField(db_column='Organism', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subcellular = models.CharField(db_column='Subcellular', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    doi_id = models.CharField(db_column='DOI_ID', max_length=4096, blank=True, null=True)  # Field name made lowercase.
    pdb = models.CharField(db_column='PDB', max_length=256, blank=True, null=True)  # Field name made lowercase.
    string = models.CharField(db_column='STRING', max_length=50, blank=True, null=True)  # Field name made lowercase.
    function_cc = models.CharField(db_column='Function_CC', max_length=8192, blank=True, null=True)  # Field name made lowercase.
    bindingdb = models.CharField(db_column='BindingDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orthodb = models.CharField(db_column='OrthoDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    expressionatlas = models.CharField(db_column='ExpressionAtlas', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Foldseek_rice'


class FoldseekSoybean(models.Model):
    uniprot_id = models.CharField(db_column='Uniprot_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    query = models.CharField(max_length=50, blank=True, null=True)
    target = models.CharField(max_length=50, blank=True, null=True)
    fident = models.FloatField(blank=True, null=True)
    alnlen = models.IntegerField(blank=True, null=True)
    mismatch = models.IntegerField(blank=True, null=True)
    gapopen = models.IntegerField(blank=True, null=True)
    qstart = models.IntegerField(blank=True, null=True)
    qend = models.IntegerField(blank=True, null=True)
    tstart = models.IntegerField(blank=True, null=True)
    tend = models.IntegerField(blank=True, null=True)
    evalue = models.FloatField(blank=True, null=True)
    bits = models.IntegerField(blank=True, null=True)
    alntmscore = models.FloatField(blank=True, null=True)
    qtmscore = models.FloatField(blank=True, null=True)
    ttmscore = models.FloatField(blank=True, null=True)
    lddt = models.FloatField(blank=True, null=True)
    prob = models.FloatField(blank=True, null=True)
    pocket_id = models.CharField(db_column='Pocket_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=50, blank=True, null=True)  # Field name made lowercase.
    protein_names = models.CharField(db_column='Protein_names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    gene_names = models.CharField(db_column='Gene_names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    organism = models.CharField(db_column='Organism', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subcellular = models.CharField(db_column='Subcellular', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    doi_id = models.CharField(db_column='DOI_ID', max_length=4096, blank=True, null=True)  # Field name made lowercase.
    pdb = models.CharField(db_column='PDB', max_length=256, blank=True, null=True)  # Field name made lowercase.
    string = models.CharField(db_column='STRING', max_length=50, blank=True, null=True)  # Field name made lowercase.
    function_cc = models.CharField(db_column='Function_CC', max_length=8192, blank=True, null=True)  # Field name made lowercase.
    bindingdb = models.CharField(db_column='BindingDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orthodb = models.CharField(db_column='OrthoDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    expressionatlas = models.CharField(db_column='ExpressionAtlas', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Foldseek_soybean'


class InvresultArabidopsisAbscisicAcid(models.Model):
    pocket_id = models.CharField(db_column='Pocket_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    uniprot_id = models.CharField(db_column='Uniprot_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    afdb_id = models.CharField(db_column='AFDB_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    binding_affinity = models.FloatField(db_column='Binding_affinity', blank=True, null=True)  # Field name made lowercase.
    entry = models.CharField(db_column='Entry', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pdb = models.CharField(db_column='PDB', max_length=256, blank=True, null=True)  # Field name made lowercase.
    string = models.CharField(db_column='STRING', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bindingdb = models.CharField(db_column='BindingDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orthodb = models.CharField(db_column='OrthoDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    expressionatlas = models.CharField(db_column='ExpressionAtlas', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gene_names = models.CharField(db_column='Gene_Names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    protein_names = models.CharField(db_column='Protein_names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    organism = models.CharField(db_column='Organism', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subcellular_location = models.CharField(db_column='Subcellular_location', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    function_description = models.CharField(db_column='Function_description', max_length=8192, blank=True, null=True)  # Field name made lowercase.
    doi_id = models.CharField(db_column='DOI_ID', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    ligand_path = models.CharField(db_column='Ligand_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    receptor_path = models.CharField(db_column='Receptor_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    complex_path = models.CharField(db_column='Complex_Path', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvResult_arabidopsis_abscisic_acid'
        ordering=['binding_affinity']


class InvresultArabidopsisAuxin(models.Model):
    pocket_id = models.CharField(db_column='Pocket_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    uniprot_id = models.CharField(db_column='Uniprot_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    afdb_id = models.CharField(db_column='AFDB_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    binding_affinity = models.FloatField(db_column='Binding_affinity', blank=True, null=True)  # Field name made lowercase.
    entry = models.CharField(db_column='Entry', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pdb = models.CharField(db_column='PDB', max_length=256, blank=True, null=True)  # Field name made lowercase.
    string = models.CharField(db_column='STRING', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bindingdb = models.CharField(db_column='BindingDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orthodb = models.CharField(db_column='OrthoDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    expressionatlas = models.CharField(db_column='ExpressionAtlas', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gene_names = models.CharField(db_column='Gene_Names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    protein_names = models.CharField(db_column='Protein_names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    organism = models.CharField(db_column='Organism', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subcellular_location = models.CharField(db_column='Subcellular_location', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    function_description = models.CharField(db_column='Function_description', max_length=8192, blank=True, null=True)  # Field name made lowercase.
    doi_id = models.CharField(db_column='DOI_ID', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    ligand_path = models.CharField(db_column='Ligand_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    receptor_path = models.CharField(db_column='Receptor_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    complex_path = models.CharField(db_column='Complex_Path', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvResult_arabidopsis_auxin'
        ordering=['binding_affinity']


class InvresultArabidopsisBrassinolide(models.Model):
    pocket_id = models.CharField(db_column='Pocket_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    uniprot_id = models.CharField(db_column='Uniprot_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    afdb_id = models.CharField(db_column='AFDB_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    binding_affinity = models.FloatField(db_column='Binding_affinity', blank=True, null=True)  # Field name made lowercase.
    entry = models.CharField(db_column='Entry', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pdb = models.CharField(db_column='PDB', max_length=256, blank=True, null=True)  # Field name made lowercase.
    string = models.CharField(db_column='STRING', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bindingdb = models.CharField(db_column='BindingDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orthodb = models.CharField(db_column='OrthoDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    expressionatlas = models.CharField(db_column='ExpressionAtlas', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gene_names = models.CharField(db_column='Gene_Names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    protein_names = models.CharField(db_column='Protein_names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    organism = models.CharField(db_column='Organism', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subcellular_location = models.CharField(db_column='Subcellular_location', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    function_description = models.CharField(db_column='Function_description', max_length=8192, blank=True, null=True)  # Field name made lowercase.
    doi_id = models.CharField(db_column='DOI_ID', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    ligand_path = models.CharField(db_column='Ligand_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    receptor_path = models.CharField(db_column='Receptor_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    complex_path = models.CharField(db_column='Complex_Path', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvResult_arabidopsis_brassinolide'
        ordering=['binding_affinity']


class InvresultArabidopsisCytokinin(models.Model):
    pocket_id = models.CharField(db_column='Pocket_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    uniprot_id = models.CharField(db_column='Uniprot_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    afdb_id = models.CharField(db_column='AFDB_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    binding_affinity = models.FloatField(db_column='Binding_affinity', blank=True, null=True)  # Field name made lowercase.
    entry = models.CharField(db_column='Entry', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pdb = models.CharField(db_column='PDB', max_length=256, blank=True, null=True)  # Field name made lowercase.
    string = models.CharField(db_column='STRING', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bindingdb = models.CharField(db_column='BindingDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orthodb = models.CharField(db_column='OrthoDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    expressionatlas = models.CharField(db_column='ExpressionAtlas', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gene_names = models.CharField(db_column='Gene_Names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    protein_names = models.CharField(db_column='Protein_names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    organism = models.CharField(db_column='Organism', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subcellular_location = models.CharField(db_column='Subcellular_location', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    function_description = models.CharField(db_column='Function_description', max_length=8192, blank=True, null=True)  # Field name made lowercase.
    doi_id = models.CharField(db_column='DOI_ID', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    ligand_path = models.CharField(db_column='Ligand_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    receptor_path = models.CharField(db_column='Receptor_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    complex_path = models.CharField(db_column='Complex_Path', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvResult_arabidopsis_cytokinin'
        ordering=['binding_affinity']



class InvresultArabidopsisEthylene(models.Model):
    pocket_id = models.CharField(db_column='Pocket_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    uniprot_id = models.CharField(db_column='Uniprot_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    afdb_id = models.CharField(db_column='AFDB_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    binding_affinity = models.FloatField(db_column='Binding_affinity', blank=True, null=True)  # Field name made lowercase.
    entry = models.CharField(db_column='Entry', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pdb = models.CharField(db_column='PDB', max_length=256, blank=True, null=True)  # Field name made lowercase.
    string = models.CharField(db_column='STRING', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bindingdb = models.CharField(db_column='BindingDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orthodb = models.CharField(db_column='OrthoDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    expressionatlas = models.CharField(db_column='ExpressionAtlas', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gene_names = models.CharField(db_column='Gene_Names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    protein_names = models.CharField(db_column='Protein_names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    organism = models.CharField(db_column='Organism', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subcellular_location = models.CharField(db_column='Subcellular_location', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    function_description = models.CharField(db_column='Function_description', max_length=8192, blank=True, null=True)  # Field name made lowercase.
    doi_id = models.CharField(db_column='DOI_ID', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    ligand_path = models.CharField(db_column='Ligand_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    receptor_path = models.CharField(db_column='Receptor_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    complex_path = models.CharField(db_column='Complex_Path', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvResult_arabidopsis_ethylene'
        ordering=['binding_affinity']


class InvresultArabidopsisGibberellin(models.Model):
    pocket_id = models.CharField(db_column='Pocket_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    uniprot_id = models.CharField(db_column='Uniprot_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    afdb_id = models.CharField(db_column='AFDB_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    binding_affinity = models.FloatField(db_column='Binding_affinity', blank=True, null=True)  # Field name made lowercase.
    entry = models.CharField(db_column='Entry', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pdb = models.CharField(db_column='PDB', max_length=256, blank=True, null=True)  # Field name made lowercase.
    string = models.CharField(db_column='STRING', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bindingdb = models.CharField(db_column='BindingDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orthodb = models.CharField(db_column='OrthoDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    expressionatlas = models.CharField(db_column='ExpressionAtlas', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gene_names = models.CharField(db_column='Gene_Names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    protein_names = models.CharField(db_column='Protein_names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    organism = models.CharField(db_column='Organism', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subcellular_location = models.CharField(db_column='Subcellular_location', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    function_description = models.CharField(db_column='Function_description', max_length=8192, blank=True, null=True)  # Field name made lowercase.
    doi_id = models.CharField(db_column='DOI_ID', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    ligand_path = models.CharField(db_column='Ligand_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    receptor_path = models.CharField(db_column='Receptor_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    complex_path = models.CharField(db_column='Complex_Path', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvResult_arabidopsis_gibberellin'
        ordering=['binding_affinity']


class InvresultArabidopsisJasmonate(models.Model):
    pocket_id = models.CharField(db_column='Pocket_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    uniprot_id = models.CharField(db_column='Uniprot_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    afdb_id = models.CharField(db_column='AFDB_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    binding_affinity = models.FloatField(db_column='Binding_affinity', blank=True, null=True)  # Field name made lowercase.
    entry = models.CharField(db_column='Entry', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pdb = models.CharField(db_column='PDB', max_length=256, blank=True, null=True)  # Field name made lowercase.
    string = models.CharField(db_column='STRING', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bindingdb = models.CharField(db_column='BindingDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orthodb = models.CharField(db_column='OrthoDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    expressionatlas = models.CharField(db_column='ExpressionAtlas', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gene_names = models.CharField(db_column='Gene_Names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    protein_names = models.CharField(db_column='Protein_names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    organism = models.CharField(db_column='Organism', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subcellular_location = models.CharField(db_column='Subcellular_location', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    function_description = models.CharField(db_column='Function_description', max_length=8192, blank=True, null=True)  # Field name made lowercase.
    doi_id = models.CharField(db_column='DOI_ID', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    ligand_path = models.CharField(db_column='Ligand_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    receptor_path = models.CharField(db_column='Receptor_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    complex_path = models.CharField(db_column='Complex_Path', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvResult_arabidopsis_jasmonate'
        ordering=['binding_affinity']


class InvresultArabidopsisSalicylicAcid(models.Model):
    pocket_id = models.CharField(db_column='Pocket_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    uniprot_id = models.CharField(db_column='Uniprot_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    afdb_id = models.CharField(db_column='AFDB_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    binding_affinity = models.FloatField(db_column='Binding_affinity', blank=True, null=True)  # Field name made lowercase.
    entry = models.CharField(db_column='Entry', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pdb = models.CharField(db_column='PDB', max_length=256, blank=True, null=True)  # Field name made lowercase.
    string = models.CharField(db_column='STRING', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bindingdb = models.CharField(db_column='BindingDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orthodb = models.CharField(db_column='OrthoDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    expressionatlas = models.CharField(db_column='ExpressionAtlas', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gene_names = models.CharField(db_column='Gene_Names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    protein_names = models.CharField(db_column='Protein_names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    organism = models.CharField(db_column='Organism', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subcellular_location = models.CharField(db_column='Subcellular_location', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    function_description = models.CharField(db_column='Function_description', max_length=8192, blank=True, null=True)  # Field name made lowercase.
    doi_id = models.CharField(db_column='DOI_ID', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    ligand_path = models.CharField(db_column='Ligand_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    receptor_path = models.CharField(db_column='Receptor_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    complex_path = models.CharField(db_column='Complex_Path', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvResult_arabidopsis_salicylic_acid'
        ordering=['binding_affinity']


class InvresultArabidopsisStrigolactone(models.Model):
    pocket_id = models.CharField(db_column='Pocket_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    uniprot_id = models.CharField(db_column='Uniprot_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    afdb_id = models.CharField(db_column='AFDB_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    binding_affinity = models.FloatField(db_column='Binding_affinity', blank=True, null=True)  # Field name made lowercase.
    entry = models.CharField(db_column='Entry', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pdb = models.CharField(db_column='PDB', max_length=256, blank=True, null=True)  # Field name made lowercase.
    string = models.CharField(db_column='STRING', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bindingdb = models.CharField(db_column='BindingDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orthodb = models.CharField(db_column='OrthoDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    expressionatlas = models.CharField(db_column='ExpressionAtlas', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gene_names = models.CharField(db_column='Gene_Names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    protein_names = models.CharField(db_column='Protein_names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    organism = models.CharField(db_column='Organism', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subcellular_location = models.CharField(db_column='Subcellular_location', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    function_description = models.CharField(db_column='Function_description', max_length=8192, blank=True, null=True)  # Field name made lowercase.
    doi_id = models.CharField(db_column='DOI_ID', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    ligand_path = models.CharField(db_column='Ligand_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    receptor_path = models.CharField(db_column='Receptor_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    complex_path = models.CharField(db_column='Complex_Path', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvResult_arabidopsis_strigolactone'
        ordering=['binding_affinity']


class InvresultMaizeAbscisicAcid(models.Model):
    pocket_id = models.CharField(db_column='Pocket_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    uniprot_id = models.CharField(db_column='Uniprot_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    afdb_id = models.CharField(db_column='AFDB_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    binding_affinity = models.FloatField(db_column='Binding_affinity', blank=True, null=True)  # Field name made lowercase.
    entry = models.CharField(db_column='Entry', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pdb = models.CharField(db_column='PDB', max_length=256, blank=True, null=True)  # Field name made lowercase.
    string = models.CharField(db_column='STRING', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bindingdb = models.CharField(db_column='BindingDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orthodb = models.CharField(db_column='OrthoDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    expressionatlas = models.CharField(db_column='ExpressionAtlas', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gene_names = models.CharField(db_column='Gene_Names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    protein_names = models.CharField(db_column='Protein_names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    organism = models.CharField(db_column='Organism', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subcellular_location = models.CharField(db_column='Subcellular_location', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    function_description = models.CharField(db_column='Function_description', max_length=8192, blank=True, null=True)  # Field name made lowercase.
    doi_id = models.CharField(db_column='DOI_ID', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    ligand_path = models.CharField(db_column='Ligand_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    receptor_path = models.CharField(db_column='Receptor_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    complex_path = models.CharField(db_column='Complex_Path', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvResult_maize_abscisic_acid'
        ordering=['binding_affinity']


class InvresultMaizeAuxin(models.Model):
    pocket_id = models.CharField(db_column='Pocket_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    uniprot_id = models.CharField(db_column='Uniprot_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    afdb_id = models.CharField(db_column='AFDB_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    binding_affinity = models.FloatField(db_column='Binding_affinity', blank=True, null=True)  # Field name made lowercase.
    entry = models.CharField(db_column='Entry', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pdb = models.CharField(db_column='PDB', max_length=256, blank=True, null=True)  # Field name made lowercase.
    string = models.CharField(db_column='STRING', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bindingdb = models.CharField(db_column='BindingDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orthodb = models.CharField(db_column='OrthoDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    expressionatlas = models.CharField(db_column='ExpressionAtlas', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gene_names = models.CharField(db_column='Gene_Names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    protein_names = models.CharField(db_column='Protein_names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    organism = models.CharField(db_column='Organism', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subcellular_location = models.CharField(db_column='Subcellular_location', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    function_description = models.CharField(db_column='Function_description', max_length=8192, blank=True, null=True)  # Field name made lowercase.
    doi_id = models.CharField(db_column='DOI_ID', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    ligand_path = models.CharField(db_column='Ligand_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    receptor_path = models.CharField(db_column='Receptor_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    complex_path = models.CharField(db_column='Complex_Path', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvResult_maize_auxin'
        ordering=['binding_affinity']


class InvresultMaizeBrassinolide(models.Model):
    pocket_id = models.CharField(db_column='Pocket_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    uniprot_id = models.CharField(db_column='Uniprot_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    afdb_id = models.CharField(db_column='AFDB_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    binding_affinity = models.FloatField(db_column='Binding_affinity', blank=True, null=True)  # Field name made lowercase.
    entry = models.CharField(db_column='Entry', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pdb = models.CharField(db_column='PDB', max_length=256, blank=True, null=True)  # Field name made lowercase.
    string = models.CharField(db_column='STRING', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bindingdb = models.CharField(db_column='BindingDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orthodb = models.CharField(db_column='OrthoDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    expressionatlas = models.CharField(db_column='ExpressionAtlas', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gene_names = models.CharField(db_column='Gene_Names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    protein_names = models.CharField(db_column='Protein_names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    organism = models.CharField(db_column='Organism', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subcellular_location = models.CharField(db_column='Subcellular_location', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    function_description = models.CharField(db_column='Function_description', max_length=8192, blank=True, null=True)  # Field name made lowercase.
    doi_id = models.CharField(db_column='DOI_ID', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    ligand_path = models.CharField(db_column='Ligand_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    receptor_path = models.CharField(db_column='Receptor_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    complex_path = models.CharField(db_column='Complex_Path', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvResult_maize_brassinolide'
        ordering=['binding_affinity']


class InvresultMaizeCytokinin(models.Model):
    pocket_id = models.CharField(db_column='Pocket_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    uniprot_id = models.CharField(db_column='Uniprot_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    afdb_id = models.CharField(db_column='AFDB_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    binding_affinity = models.FloatField(db_column='Binding_affinity', blank=True, null=True)  # Field name made lowercase.
    entry = models.CharField(db_column='Entry', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pdb = models.CharField(db_column='PDB', max_length=256, blank=True, null=True)  # Field name made lowercase.
    string = models.CharField(db_column='STRING', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bindingdb = models.CharField(db_column='BindingDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orthodb = models.CharField(db_column='OrthoDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    expressionatlas = models.CharField(db_column='ExpressionAtlas', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gene_names = models.CharField(db_column='Gene_Names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    protein_names = models.CharField(db_column='Protein_names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    organism = models.CharField(db_column='Organism', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subcellular_location = models.CharField(db_column='Subcellular_location', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    function_description = models.CharField(db_column='Function_description', max_length=8192, blank=True, null=True)  # Field name made lowercase.
    doi_id = models.CharField(db_column='DOI_ID', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    ligand_path = models.CharField(db_column='Ligand_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    receptor_path = models.CharField(db_column='Receptor_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    complex_path = models.CharField(db_column='Complex_Path', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvResult_maize_cytokinin'
        ordering=['binding_affinity']


class InvresultMaizeEthylene(models.Model):
    pocket_id = models.CharField(db_column='Pocket_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    uniprot_id = models.CharField(db_column='Uniprot_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    afdb_id = models.CharField(db_column='AFDB_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    binding_affinity = models.FloatField(db_column='Binding_affinity', blank=True, null=True)  # Field name made lowercase.
    entry = models.CharField(db_column='Entry', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pdb = models.CharField(db_column='PDB', max_length=256, blank=True, null=True)  # Field name made lowercase.
    string = models.CharField(db_column='STRING', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bindingdb = models.CharField(db_column='BindingDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orthodb = models.CharField(db_column='OrthoDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    expressionatlas = models.CharField(db_column='ExpressionAtlas', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gene_names = models.CharField(db_column='Gene_Names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    protein_names = models.CharField(db_column='Protein_names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    organism = models.CharField(db_column='Organism', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subcellular_location = models.CharField(db_column='Subcellular_location', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    function_description = models.CharField(db_column='Function_description', max_length=8192, blank=True, null=True)  # Field name made lowercase.
    doi_id = models.CharField(db_column='DOI_ID', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    ligand_path = models.CharField(db_column='Ligand_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    receptor_path = models.CharField(db_column='Receptor_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    complex_path = models.CharField(db_column='Complex_Path', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvResult_maize_ethylene'
        ordering=['binding_affinity']


class InvresultMaizeGibberellin(models.Model):
    pocket_id = models.CharField(db_column='Pocket_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    uniprot_id = models.CharField(db_column='Uniprot_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    afdb_id = models.CharField(db_column='AFDB_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    binding_affinity = models.FloatField(db_column='Binding_affinity', blank=True, null=True)  # Field name made lowercase.
    entry = models.CharField(db_column='Entry', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pdb = models.CharField(db_column='PDB', max_length=256, blank=True, null=True)  # Field name made lowercase.
    string = models.CharField(db_column='STRING', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bindingdb = models.CharField(db_column='BindingDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orthodb = models.CharField(db_column='OrthoDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    expressionatlas = models.CharField(db_column='ExpressionAtlas', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gene_names = models.CharField(db_column='Gene_Names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    protein_names = models.CharField(db_column='Protein_names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    organism = models.CharField(db_column='Organism', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subcellular_location = models.CharField(db_column='Subcellular_location', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    function_description = models.CharField(db_column='Function_description', max_length=8192, blank=True, null=True)  # Field name made lowercase.
    doi_id = models.CharField(db_column='DOI_ID', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    ligand_path = models.CharField(db_column='Ligand_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    receptor_path = models.CharField(db_column='Receptor_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    complex_path = models.CharField(db_column='Complex_Path', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvResult_maize_gibberellin'
        ordering=['binding_affinity']


class InvresultMaizeJasmonate(models.Model):
    pocket_id = models.CharField(db_column='Pocket_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    uniprot_id = models.CharField(db_column='Uniprot_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    afdb_id = models.CharField(db_column='AFDB_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    binding_affinity = models.FloatField(db_column='Binding_affinity', blank=True, null=True)  # Field name made lowercase.
    entry = models.CharField(db_column='Entry', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pdb = models.CharField(db_column='PDB', max_length=256, blank=True, null=True)  # Field name made lowercase.
    string = models.CharField(db_column='STRING', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bindingdb = models.CharField(db_column='BindingDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orthodb = models.CharField(db_column='OrthoDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    expressionatlas = models.CharField(db_column='ExpressionAtlas', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gene_names = models.CharField(db_column='Gene_Names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    protein_names = models.CharField(db_column='Protein_names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    organism = models.CharField(db_column='Organism', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subcellular_location = models.CharField(db_column='Subcellular_location', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    function_description = models.CharField(db_column='Function_description', max_length=8192, blank=True, null=True)  # Field name made lowercase.
    doi_id = models.CharField(db_column='DOI_ID', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    ligand_path = models.CharField(db_column='Ligand_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    receptor_path = models.CharField(db_column='Receptor_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    complex_path = models.CharField(db_column='Complex_Path', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvResult_maize_jasmonate'
        ordering=['binding_affinity']


class InvresultMaizeSalicylicAcid(models.Model):
    pocket_id = models.CharField(db_column='Pocket_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    uniprot_id = models.CharField(db_column='Uniprot_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    afdb_id = models.CharField(db_column='AFDB_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    binding_affinity = models.FloatField(db_column='Binding_affinity', blank=True, null=True)  # Field name made lowercase.
    entry = models.CharField(db_column='Entry', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pdb = models.CharField(db_column='PDB', max_length=256, blank=True, null=True)  # Field name made lowercase.
    string = models.CharField(db_column='STRING', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bindingdb = models.CharField(db_column='BindingDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orthodb = models.CharField(db_column='OrthoDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    expressionatlas = models.CharField(db_column='ExpressionAtlas', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gene_names = models.CharField(db_column='Gene_Names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    protein_names = models.CharField(db_column='Protein_names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    organism = models.CharField(db_column='Organism', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subcellular_location = models.CharField(db_column='Subcellular_location', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    function_description = models.CharField(db_column='Function_description', max_length=8192, blank=True, null=True)  # Field name made lowercase.
    doi_id = models.CharField(db_column='DOI_ID', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    ligand_path = models.CharField(db_column='Ligand_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    receptor_path = models.CharField(db_column='Receptor_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    complex_path = models.CharField(db_column='Complex_Path', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvResult_maize_salicylic_acid'
        ordering=['binding_affinity']


class InvresultMaizeStrigolactone(models.Model):
    pocket_id = models.CharField(db_column='Pocket_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    uniprot_id = models.CharField(db_column='Uniprot_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    afdb_id = models.CharField(db_column='AFDB_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    binding_affinity = models.FloatField(db_column='Binding_affinity', blank=True, null=True)  # Field name made lowercase.
    entry = models.CharField(db_column='Entry', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pdb = models.CharField(db_column='PDB', max_length=256, blank=True, null=True)  # Field name made lowercase.
    string = models.CharField(db_column='STRING', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bindingdb = models.CharField(db_column='BindingDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orthodb = models.CharField(db_column='OrthoDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    expressionatlas = models.CharField(db_column='ExpressionAtlas', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gene_names = models.CharField(db_column='Gene_Names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    protein_names = models.CharField(db_column='Protein_names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    organism = models.CharField(db_column='Organism', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subcellular_location = models.CharField(db_column='Subcellular_location', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    function_description = models.CharField(db_column='Function_description', max_length=8192, blank=True, null=True)  # Field name made lowercase.
    doi_id = models.CharField(db_column='DOI_ID', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    ligand_path = models.CharField(db_column='Ligand_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    receptor_path = models.CharField(db_column='Receptor_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    complex_path = models.CharField(db_column='Complex_Path', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvResult_maize_strigolactone'
        ordering=['binding_affinity']


class InvresultRiceAbscisicAcid(models.Model):
    pocket_id = models.CharField(db_column='Pocket_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    uniprot_id = models.CharField(db_column='Uniprot_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    afdb_id = models.CharField(db_column='AFDB_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    binding_affinity = models.FloatField(db_column='Binding_affinity', blank=True, null=True)  # Field name made lowercase.
    entry = models.CharField(db_column='Entry', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pdb = models.CharField(db_column='PDB', max_length=256, blank=True, null=True)  # Field name made lowercase.
    string = models.CharField(db_column='STRING', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bindingdb = models.CharField(db_column='BindingDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orthodb = models.CharField(db_column='OrthoDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    expressionatlas = models.CharField(db_column='ExpressionAtlas', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gene_names = models.CharField(db_column='Gene_Names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    protein_names = models.CharField(db_column='Protein_names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    organism = models.CharField(db_column='Organism', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subcellular_location = models.CharField(db_column='Subcellular_location', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    function_description = models.CharField(db_column='Function_description', max_length=8192, blank=True, null=True)  # Field name made lowercase.
    doi_id = models.CharField(db_column='DOI_ID', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    ligand_path = models.CharField(db_column='Ligand_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    receptor_path = models.CharField(db_column='Receptor_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    complex_path = models.CharField(db_column='Complex_Path', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvResult_rice_abscisic_acid'
        ordering=['binding_affinity']


class InvresultRiceAuxin(models.Model):
    pocket_id = models.CharField(db_column='Pocket_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    uniprot_id = models.CharField(db_column='Uniprot_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    afdb_id = models.CharField(db_column='AFDB_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    binding_affinity = models.FloatField(db_column='Binding_affinity', blank=True, null=True)  # Field name made lowercase.
    entry = models.CharField(db_column='Entry', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pdb = models.CharField(db_column='PDB', max_length=256, blank=True, null=True)  # Field name made lowercase.
    string = models.CharField(db_column='STRING', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bindingdb = models.CharField(db_column='BindingDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orthodb = models.CharField(db_column='OrthoDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    expressionatlas = models.CharField(db_column='ExpressionAtlas', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gene_names = models.CharField(db_column='Gene_Names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    protein_names = models.CharField(db_column='Protein_names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    organism = models.CharField(db_column='Organism', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subcellular_location = models.CharField(db_column='Subcellular_location', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    function_description = models.CharField(db_column='Function_description', max_length=8192, blank=True, null=True)  # Field name made lowercase.
    doi_id = models.CharField(db_column='DOI_ID', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    ligand_path = models.CharField(db_column='Ligand_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    receptor_path = models.CharField(db_column='Receptor_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    complex_path = models.CharField(db_column='Complex_Path', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvResult_rice_auxin'
        ordering=['binding_affinity']


class InvresultRiceBrassinolide(models.Model):
    pocket_id = models.CharField(db_column='Pocket_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    uniprot_id = models.CharField(db_column='Uniprot_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    afdb_id = models.CharField(db_column='AFDB_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    binding_affinity = models.FloatField(db_column='Binding_affinity', blank=True, null=True)  # Field name made lowercase.
    entry = models.CharField(db_column='Entry', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pdb = models.CharField(db_column='PDB', max_length=256, blank=True, null=True)  # Field name made lowercase.
    string = models.CharField(db_column='STRING', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bindingdb = models.CharField(db_column='BindingDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orthodb = models.CharField(db_column='OrthoDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    expressionatlas = models.CharField(db_column='ExpressionAtlas', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gene_names = models.CharField(db_column='Gene_Names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    protein_names = models.CharField(db_column='Protein_names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    organism = models.CharField(db_column='Organism', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subcellular_location = models.CharField(db_column='Subcellular_location', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    function_description = models.CharField(db_column='Function_description', max_length=8192, blank=True, null=True)  # Field name made lowercase.
    doi_id = models.CharField(db_column='DOI_ID', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    ligand_path = models.CharField(db_column='Ligand_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    receptor_path = models.CharField(db_column='Receptor_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    complex_path = models.CharField(db_column='Complex_Path', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvResult_rice_brassinolide'
        ordering=['binding_affinity']


class InvresultRiceCytokinin(models.Model):
    pocket_id = models.CharField(db_column='Pocket_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    uniprot_id = models.CharField(db_column='Uniprot_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    afdb_id = models.CharField(db_column='AFDB_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    binding_affinity = models.FloatField(db_column='Binding_affinity', blank=True, null=True)  # Field name made lowercase.
    entry = models.CharField(db_column='Entry', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pdb = models.CharField(db_column='PDB', max_length=256, blank=True, null=True)  # Field name made lowercase.
    string = models.CharField(db_column='STRING', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bindingdb = models.CharField(db_column='BindingDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orthodb = models.CharField(db_column='OrthoDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    expressionatlas = models.CharField(db_column='ExpressionAtlas', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gene_names = models.CharField(db_column='Gene_Names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    protein_names = models.CharField(db_column='Protein_names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    organism = models.CharField(db_column='Organism', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subcellular_location = models.CharField(db_column='Subcellular_location', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    function_description = models.CharField(db_column='Function_description', max_length=8192, blank=True, null=True)  # Field name made lowercase.
    doi_id = models.CharField(db_column='DOI_ID', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    ligand_path = models.CharField(db_column='Ligand_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    receptor_path = models.CharField(db_column='Receptor_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    complex_path = models.CharField(db_column='Complex_Path', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvResult_rice_cytokinin'
        ordering=['binding_affinity']


class InvresultRiceEthylene(models.Model):
    pocket_id = models.CharField(db_column='Pocket_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    uniprot_id = models.CharField(db_column='Uniprot_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    afdb_id = models.CharField(db_column='AFDB_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    binding_affinity = models.FloatField(db_column='Binding_affinity', blank=True, null=True)  # Field name made lowercase.
    entry = models.CharField(db_column='Entry', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pdb = models.CharField(db_column='PDB', max_length=256, blank=True, null=True)  # Field name made lowercase.
    string = models.CharField(db_column='STRING', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bindingdb = models.CharField(db_column='BindingDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orthodb = models.CharField(db_column='OrthoDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    expressionatlas = models.CharField(db_column='ExpressionAtlas', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gene_names = models.CharField(db_column='Gene_Names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    protein_names = models.CharField(db_column='Protein_names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    organism = models.CharField(db_column='Organism', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subcellular_location = models.CharField(db_column='Subcellular_location', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    function_description = models.CharField(db_column='Function_description', max_length=8192, blank=True, null=True)  # Field name made lowercase.
    doi_id = models.CharField(db_column='DOI_ID', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    ligand_path = models.CharField(db_column='Ligand_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    receptor_path = models.CharField(db_column='Receptor_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    complex_path = models.CharField(db_column='Complex_Path', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvResult_rice_ethylene'
        ordering=['binding_affinity']


class InvresultRiceGibberellin(models.Model):
    pocket_id = models.CharField(db_column='Pocket_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    uniprot_id = models.CharField(db_column='Uniprot_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    afdb_id = models.CharField(db_column='AFDB_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    binding_affinity = models.FloatField(db_column='Binding_affinity', blank=True, null=True)  # Field name made lowercase.
    entry = models.CharField(db_column='Entry', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pdb = models.CharField(db_column='PDB', max_length=256, blank=True, null=True)  # Field name made lowercase.
    string = models.CharField(db_column='STRING', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bindingdb = models.CharField(db_column='BindingDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orthodb = models.CharField(db_column='OrthoDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    expressionatlas = models.CharField(db_column='ExpressionAtlas', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gene_names = models.CharField(db_column='Gene_Names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    protein_names = models.CharField(db_column='Protein_names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    organism = models.CharField(db_column='Organism', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subcellular_location = models.CharField(db_column='Subcellular_location', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    function_description = models.CharField(db_column='Function_description', max_length=8192, blank=True, null=True)  # Field name made lowercase.
    doi_id = models.CharField(db_column='DOI_ID', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    ligand_path = models.CharField(db_column='Ligand_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    receptor_path = models.CharField(db_column='Receptor_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    complex_path = models.CharField(db_column='Complex_Path', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvResult_rice_gibberellin'
        ordering=['binding_affinity']


class InvresultRiceJasmonate(models.Model):
    pocket_id = models.CharField(db_column='Pocket_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    uniprot_id = models.CharField(db_column='Uniprot_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    afdb_id = models.CharField(db_column='AFDB_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    binding_affinity = models.FloatField(db_column='Binding_affinity', blank=True, null=True)  # Field name made lowercase.
    entry = models.CharField(db_column='Entry', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pdb = models.CharField(db_column='PDB', max_length=256, blank=True, null=True)  # Field name made lowercase.
    string = models.CharField(db_column='STRING', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bindingdb = models.CharField(db_column='BindingDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orthodb = models.CharField(db_column='OrthoDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    expressionatlas = models.CharField(db_column='ExpressionAtlas', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gene_names = models.CharField(db_column='Gene_Names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    protein_names = models.CharField(db_column='Protein_names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    organism = models.CharField(db_column='Organism', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subcellular_location = models.CharField(db_column='Subcellular_location', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    function_description = models.CharField(db_column='Function_description', max_length=8192, blank=True, null=True)  # Field name made lowercase.
    doi_id = models.CharField(db_column='DOI_ID', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    ligand_path = models.CharField(db_column='Ligand_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    receptor_path = models.CharField(db_column='Receptor_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    complex_path = models.CharField(db_column='Complex_Path', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvResult_rice_jasmonate'
        ordering=['binding_affinity']


class InvresultRiceSalicylicAcid(models.Model):
    pocket_id = models.CharField(db_column='Pocket_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    uniprot_id = models.CharField(db_column='Uniprot_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    afdb_id = models.CharField(db_column='AFDB_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    binding_affinity = models.FloatField(db_column='Binding_affinity', blank=True, null=True)  # Field name made lowercase.
    entry = models.CharField(db_column='Entry', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pdb = models.CharField(db_column='PDB', max_length=256, blank=True, null=True)  # Field name made lowercase.
    string = models.CharField(db_column='STRING', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bindingdb = models.CharField(db_column='BindingDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orthodb = models.CharField(db_column='OrthoDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    expressionatlas = models.CharField(db_column='ExpressionAtlas', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gene_names = models.CharField(db_column='Gene_Names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    protein_names = models.CharField(db_column='Protein_names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    organism = models.CharField(db_column='Organism', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subcellular_location = models.CharField(db_column='Subcellular_location', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    function_description = models.CharField(db_column='Function_description', max_length=8192, blank=True, null=True)  # Field name made lowercase.
    doi_id = models.CharField(db_column='DOI_ID', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    ligand_path = models.CharField(db_column='Ligand_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    receptor_path = models.CharField(db_column='Receptor_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    complex_path = models.CharField(db_column='Complex_Path', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvResult_rice_salicylic_acid'
        ordering=['binding_affinity']


class InvresultRiceStrigolactone(models.Model):
    pocket_id = models.CharField(db_column='Pocket_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    uniprot_id = models.CharField(db_column='Uniprot_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    afdb_id = models.CharField(db_column='AFDB_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    binding_affinity = models.FloatField(db_column='Binding_affinity', blank=True, null=True)  # Field name made lowercase.
    entry = models.CharField(db_column='Entry', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pdb = models.CharField(db_column='PDB', max_length=256, blank=True, null=True)  # Field name made lowercase.
    string = models.CharField(db_column='STRING', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bindingdb = models.CharField(db_column='BindingDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orthodb = models.CharField(db_column='OrthoDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    expressionatlas = models.CharField(db_column='ExpressionAtlas', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gene_names = models.CharField(db_column='Gene_Names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    protein_names = models.CharField(db_column='Protein_names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    organism = models.CharField(db_column='Organism', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subcellular_location = models.CharField(db_column='Subcellular_location', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    function_description = models.CharField(db_column='Function_description', max_length=8192, blank=True, null=True)  # Field name made lowercase.
    doi_id = models.CharField(db_column='DOI_ID', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    ligand_path = models.CharField(db_column='Ligand_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    receptor_path = models.CharField(db_column='Receptor_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    complex_path = models.CharField(db_column='Complex_Path', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvResult_rice_strigolactone'
        ordering=['binding_affinity']


class InvresultSoybeanAbscisicAcid(models.Model):
    pocket_id = models.CharField(db_column='Pocket_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    uniprot_id = models.CharField(db_column='Uniprot_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    afdb_id = models.CharField(db_column='AFDB_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    binding_affinity = models.FloatField(db_column='Binding_affinity', blank=True, null=True)  # Field name made lowercase.
    entry = models.CharField(db_column='Entry', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pdb = models.CharField(db_column='PDB', max_length=256, blank=True, null=True)  # Field name made lowercase.
    string = models.CharField(db_column='STRING', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bindingdb = models.CharField(db_column='BindingDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orthodb = models.CharField(db_column='OrthoDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    expressionatlas = models.CharField(db_column='ExpressionAtlas', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gene_names = models.CharField(db_column='Gene_Names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    protein_names = models.CharField(db_column='Protein_names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    organism = models.CharField(db_column='Organism', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subcellular_location = models.CharField(db_column='Subcellular_location', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    function_description = models.CharField(db_column='Function_description', max_length=8192, blank=True, null=True)  # Field name made lowercase.
    doi_id = models.CharField(db_column='DOI_ID', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    ligand_path = models.CharField(db_column='Ligand_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    receptor_path = models.CharField(db_column='Receptor_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    complex_path = models.CharField(db_column='Complex_Path', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvResult_soybean_abscisic_acid'
        ordering=['binding_affinity']


class InvresultSoybeanAuxin(models.Model):
    pocket_id = models.CharField(db_column='Pocket_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    uniprot_id = models.CharField(db_column='Uniprot_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    afdb_id = models.CharField(db_column='AFDB_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    binding_affinity = models.FloatField(db_column='Binding_affinity', blank=True, null=True)  # Field name made lowercase.
    entry = models.CharField(db_column='Entry', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pdb = models.CharField(db_column='PDB', max_length=256, blank=True, null=True)  # Field name made lowercase.
    string = models.CharField(db_column='STRING', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bindingdb = models.CharField(db_column='BindingDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orthodb = models.CharField(db_column='OrthoDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    expressionatlas = models.CharField(db_column='ExpressionAtlas', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gene_names = models.CharField(db_column='Gene_Names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    protein_names = models.CharField(db_column='Protein_names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    organism = models.CharField(db_column='Organism', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subcellular_location = models.CharField(db_column='Subcellular_location', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    function_description = models.CharField(db_column='Function_description', max_length=8192, blank=True, null=True)  # Field name made lowercase.
    doi_id = models.CharField(db_column='DOI_ID', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    ligand_path = models.CharField(db_column='Ligand_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    receptor_path = models.CharField(db_column='Receptor_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    complex_path = models.CharField(db_column='Complex_Path', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvResult_soybean_auxin'
        ordering=['binding_affinity']


class InvresultSoybeanBrassinolide(models.Model):
    pocket_id = models.CharField(db_column='Pocket_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    uniprot_id = models.CharField(db_column='Uniprot_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    afdb_id = models.CharField(db_column='AFDB_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    binding_affinity = models.FloatField(db_column='Binding_affinity', blank=True, null=True)  # Field name made lowercase.
    entry = models.CharField(db_column='Entry', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pdb = models.CharField(db_column='PDB', max_length=256, blank=True, null=True)  # Field name made lowercase.
    string = models.CharField(db_column='STRING', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bindingdb = models.CharField(db_column='BindingDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orthodb = models.CharField(db_column='OrthoDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    expressionatlas = models.CharField(db_column='ExpressionAtlas', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gene_names = models.CharField(db_column='Gene_Names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    protein_names = models.CharField(db_column='Protein_names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    organism = models.CharField(db_column='Organism', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subcellular_location = models.CharField(db_column='Subcellular_location', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    function_description = models.CharField(db_column='Function_description', max_length=8192, blank=True, null=True)  # Field name made lowercase.
    doi_id = models.CharField(db_column='DOI_ID', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    ligand_path = models.CharField(db_column='Ligand_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    receptor_path = models.CharField(db_column='Receptor_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    complex_path = models.CharField(db_column='Complex_Path', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvResult_soybean_brassinolide'
        ordering=['binding_affinity']


class InvresultSoybeanCytokinin(models.Model):
    pocket_id = models.CharField(db_column='Pocket_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    uniprot_id = models.CharField(db_column='Uniprot_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    afdb_id = models.CharField(db_column='AFDB_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    binding_affinity = models.FloatField(db_column='Binding_affinity', blank=True, null=True)  # Field name made lowercase.
    entry = models.CharField(db_column='Entry', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pdb = models.CharField(db_column='PDB', max_length=256, blank=True, null=True)  # Field name made lowercase.
    string = models.CharField(db_column='STRING', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bindingdb = models.CharField(db_column='BindingDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orthodb = models.CharField(db_column='OrthoDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    expressionatlas = models.CharField(db_column='ExpressionAtlas', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gene_names = models.CharField(db_column='Gene_Names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    protein_names = models.CharField(db_column='Protein_names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    organism = models.CharField(db_column='Organism', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subcellular_location = models.CharField(db_column='Subcellular_location', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    function_description = models.CharField(db_column='Function_description', max_length=8192, blank=True, null=True)  # Field name made lowercase.
    doi_id = models.CharField(db_column='DOI_ID', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    ligand_path = models.CharField(db_column='Ligand_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    receptor_path = models.CharField(db_column='Receptor_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    complex_path = models.CharField(db_column='Complex_Path', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvResult_soybean_cytokinin'
        ordering=['binding_affinity']


class InvresultSoybeanEthylene(models.Model):
    pocket_id = models.CharField(db_column='Pocket_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    uniprot_id = models.CharField(db_column='Uniprot_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    afdb_id = models.CharField(db_column='AFDB_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    binding_affinity = models.FloatField(db_column='Binding_affinity', blank=True, null=True)  # Field name made lowercase.
    entry = models.CharField(db_column='Entry', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pdb = models.CharField(db_column='PDB', max_length=256, blank=True, null=True)  # Field name made lowercase.
    string = models.CharField(db_column='STRING', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bindingdb = models.CharField(db_column='BindingDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orthodb = models.CharField(db_column='OrthoDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    expressionatlas = models.CharField(db_column='ExpressionAtlas', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gene_names = models.CharField(db_column='Gene_Names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    protein_names = models.CharField(db_column='Protein_names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    organism = models.CharField(db_column='Organism', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subcellular_location = models.CharField(db_column='Subcellular_location', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    function_description = models.CharField(db_column='Function_description', max_length=8192, blank=True, null=True)  # Field name made lowercase.
    doi_id = models.CharField(db_column='DOI_ID', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    ligand_path = models.CharField(db_column='Ligand_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    receptor_path = models.CharField(db_column='Receptor_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    complex_path = models.CharField(db_column='Complex_Path', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvResult_soybean_ethylene'
        ordering=['binding_affinity']


class InvresultSoybeanGibberellin(models.Model):
    pocket_id = models.CharField(db_column='Pocket_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    uniprot_id = models.CharField(db_column='Uniprot_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    afdb_id = models.CharField(db_column='AFDB_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    binding_affinity = models.FloatField(db_column='Binding_affinity', blank=True, null=True)  # Field name made lowercase.
    entry = models.CharField(db_column='Entry', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pdb = models.CharField(db_column='PDB', max_length=256, blank=True, null=True)  # Field name made lowercase.
    string = models.CharField(db_column='STRING', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bindingdb = models.CharField(db_column='BindingDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orthodb = models.CharField(db_column='OrthoDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    expressionatlas = models.CharField(db_column='ExpressionAtlas', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gene_names = models.CharField(db_column='Gene_Names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    protein_names = models.CharField(db_column='Protein_names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    organism = models.CharField(db_column='Organism', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subcellular_location = models.CharField(db_column='Subcellular_location', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    function_description = models.CharField(db_column='Function_description', max_length=8192, blank=True, null=True)  # Field name made lowercase.
    doi_id = models.CharField(db_column='DOI_ID', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    ligand_path = models.CharField(db_column='Ligand_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    receptor_path = models.CharField(db_column='Receptor_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    complex_path = models.CharField(db_column='Complex_Path', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvResult_soybean_gibberellin'
        ordering=['binding_affinity']


class InvresultSoybeanJasmonate(models.Model):
    pocket_id = models.CharField(db_column='Pocket_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    uniprot_id = models.CharField(db_column='Uniprot_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    afdb_id = models.CharField(db_column='AFDB_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    binding_affinity = models.FloatField(db_column='Binding_affinity', blank=True, null=True)  # Field name made lowercase.
    entry = models.CharField(db_column='Entry', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pdb = models.CharField(db_column='PDB', max_length=256, blank=True, null=True)  # Field name made lowercase.
    string = models.CharField(db_column='STRING', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bindingdb = models.CharField(db_column='BindingDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orthodb = models.CharField(db_column='OrthoDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    expressionatlas = models.CharField(db_column='ExpressionAtlas', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gene_names = models.CharField(db_column='Gene_Names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    protein_names = models.CharField(db_column='Protein_names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    organism = models.CharField(db_column='Organism', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subcellular_location = models.CharField(db_column='Subcellular_location', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    function_description = models.CharField(db_column='Function_description', max_length=8192, blank=True, null=True)  # Field name made lowercase.
    doi_id = models.CharField(db_column='DOI_ID', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    ligand_path = models.CharField(db_column='Ligand_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    receptor_path = models.CharField(db_column='Receptor_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    complex_path = models.CharField(db_column='Complex_Path', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvResult_soybean_jasmonate'
        ordering=['binding_affinity']


class InvresultSoybeanSalicylicAcid(models.Model):
    pocket_id = models.CharField(db_column='Pocket_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    uniprot_id = models.CharField(db_column='Uniprot_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    afdb_id = models.CharField(db_column='AFDB_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    binding_affinity = models.FloatField(db_column='Binding_affinity', blank=True, null=True)  # Field name made lowercase.
    entry = models.CharField(db_column='Entry', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pdb = models.CharField(db_column='PDB', max_length=256, blank=True, null=True)  # Field name made lowercase.
    string = models.CharField(db_column='STRING', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bindingdb = models.CharField(db_column='BindingDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orthodb = models.CharField(db_column='OrthoDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    expressionatlas = models.CharField(db_column='ExpressionAtlas', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gene_names = models.CharField(db_column='Gene_Names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    protein_names = models.CharField(db_column='Protein_names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    organism = models.CharField(db_column='Organism', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subcellular_location = models.CharField(db_column='Subcellular_location', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    function_description = models.CharField(db_column='Function_description', max_length=8192, blank=True, null=True)  # Field name made lowercase.
    doi_id = models.CharField(db_column='DOI_ID', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    ligand_path = models.CharField(db_column='Ligand_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    receptor_path = models.CharField(db_column='Receptor_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    complex_path = models.CharField(db_column='Complex_Path', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvResult_soybean_salicylic_acid'
        ordering=['binding_affinity']


class InvresultSoybeanStrigolactone(models.Model):
    pocket_id = models.CharField(db_column='Pocket_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    uniprot_id = models.CharField(db_column='Uniprot_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    afdb_id = models.CharField(db_column='AFDB_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    binding_affinity = models.FloatField(db_column='Binding_affinity', blank=True, null=True)  # Field name made lowercase.
    entry = models.CharField(db_column='Entry', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pdb = models.CharField(db_column='PDB', max_length=256, blank=True, null=True)  # Field name made lowercase.
    string = models.CharField(db_column='STRING', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bindingdb = models.CharField(db_column='BindingDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orthodb = models.CharField(db_column='OrthoDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    expressionatlas = models.CharField(db_column='ExpressionAtlas', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gene_names = models.CharField(db_column='Gene_Names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    protein_names = models.CharField(db_column='Protein_names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    organism = models.CharField(db_column='Organism', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subcellular_location = models.CharField(db_column='Subcellular_location', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    function_description = models.CharField(db_column='Function_description', max_length=8192, blank=True, null=True)  # Field name made lowercase.
    doi_id = models.CharField(db_column='DOI_ID', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    ligand_path = models.CharField(db_column='Ligand_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    receptor_path = models.CharField(db_column='Receptor_path', max_length=128, blank=True, null=True)  # Field name made lowercase.
    complex_path = models.CharField(db_column='Complex_Path', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvResult_soybean_strigolactone'
        ordering=['binding_affinity']


class Mmseqs2Arabidopsis(models.Model):
    target = models.CharField(db_column='Target', max_length=50)  # Field name made lowercase.
    query = models.CharField(db_column='Query', max_length=50)  # Field name made lowercase.
    sequence_identity = models.FloatField(db_column='Sequence_identity', blank=True, null=True)  # Field name made lowercase.
    alignment_length = models.IntegerField(db_column='Alignment_length', blank=True, null=True)  # Field name made lowercase.
    number_of_mismatches = models.IntegerField(db_column='Number_of_mismatches', blank=True, null=True)  # Field name made lowercase.
    number_of_gap_openings = models.IntegerField(db_column='Number_of_gap_openings', blank=True, null=True)  # Field name made lowercase.
    start_position_in_query = models.IntegerField(db_column='Start_position_in_query', blank=True, null=True)  # Field name made lowercase.
    end_position_in_query = models.IntegerField(db_column='End_position_in_query', blank=True, null=True)  # Field name made lowercase.
    start_position_in_target = models.IntegerField(db_column='Start_position_in_target', blank=True, null=True)  # Field name made lowercase.
    end_position_in_target = models.IntegerField(db_column='End_position_in_target', blank=True, null=True)  # Field name made lowercase.
    evalue = models.FloatField(db_column='Evalue', blank=True, null=True)  # Field name made lowercase.
    bit_scroe = models.IntegerField(db_column='Bit_scroe', blank=True, null=True)  # Field name made lowercase.
    pocket_id = models.CharField(db_column='Pocket_ID', max_length=50)  # Field name made lowercase.
    protein_name = models.CharField(db_column='Protein_name', max_length=512, blank=True, null=True)  # Field name made lowercase.
    n = models.CharField(max_length=128, blank=True, null=True)
    taxonomy = models.CharField(db_column='Taxonomy', max_length=512, blank=True, null=True)  # Field name made lowercase.
    taxid = models.CharField(db_column='TaxID', max_length=128, blank=True, null=True)  # Field name made lowercase.
    repid = models.CharField(db_column='RepID', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MMseqs2_arabidopsis'


class Mmseqs2Maize(models.Model):
    target = models.CharField(db_column='Target', max_length=50, blank=True, null=True)  # Field name made lowercase.
    query = models.CharField(db_column='Query', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sequence_identity = models.FloatField(db_column='Sequence_identity', blank=True, null=True)  # Field name made lowercase.
    alignment_length = models.IntegerField(db_column='Alignment_length', blank=True, null=True)  # Field name made lowercase.
    number_of_mismatches = models.IntegerField(db_column='Number_of_mismatches', blank=True, null=True)  # Field name made lowercase.
    number_of_gap_openings = models.IntegerField(db_column='Number_of_gap_openings', blank=True, null=True)  # Field name made lowercase.
    start_position_in_query = models.IntegerField(db_column='Start_position_in_query', blank=True, null=True)  # Field name made lowercase.
    end_position_in_query = models.IntegerField(db_column='End_position_in_query', blank=True, null=True)  # Field name made lowercase.
    start_position_in_target = models.IntegerField(db_column='Start_position_in_target', blank=True, null=True)  # Field name made lowercase.
    end_position_in_target = models.IntegerField(db_column='End_position_in_target', blank=True, null=True)  # Field name made lowercase.
    evalue = models.FloatField(db_column='Evalue', blank=True, null=True)  # Field name made lowercase.
    bit_scroe = models.IntegerField(db_column='Bit_scroe', blank=True, null=True)  # Field name made lowercase.
    pocket_id = models.CharField(db_column='Pocket_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    protein_name = models.CharField(db_column='Protein_name', max_length=256, blank=True, null=True)  # Field name made lowercase.
    n = models.CharField(max_length=128, blank=True, null=True)
    taxonomy = models.CharField(db_column='Taxonomy', max_length=256, blank=True, null=True)  # Field name made lowercase.
    taxid = models.CharField(db_column='TaxID', max_length=128, blank=True, null=True)  # Field name made lowercase.
    repid = models.CharField(db_column='RepID', max_length=256, blank=True, null=True)  # Field name made lowercase.
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'MMseqs2_maize'


class Mmseqs2Rice(models.Model):
    target = models.CharField(db_column='Target', max_length=50, blank=True, null=True)  # Field name made lowercase.
    query = models.CharField(db_column='Query', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sequence_identity = models.FloatField(db_column='Sequence_identity', blank=True, null=True)  # Field name made lowercase.
    alignment_length = models.IntegerField(db_column='Alignment_length', blank=True, null=True)  # Field name made lowercase.
    number_of_mismatches = models.IntegerField(db_column='Number_of_mismatches', blank=True, null=True)  # Field name made lowercase.
    number_of_gap_openings = models.IntegerField(db_column='Number_of_gap_openings', blank=True, null=True)  # Field name made lowercase.
    start_position_in_query = models.IntegerField(db_column='Start_position_in_query', blank=True, null=True)  # Field name made lowercase.
    end_position_in_query = models.IntegerField(db_column='End_position_in_query', blank=True, null=True)  # Field name made lowercase.
    start_position_in_target = models.IntegerField(db_column='Start_position_in_target', blank=True, null=True)  # Field name made lowercase.
    end_position_in_target = models.IntegerField(db_column='End_position_in_target', blank=True, null=True)  # Field name made lowercase.
    evalue = models.FloatField(db_column='Evalue', blank=True, null=True)  # Field name made lowercase.
    bit_scroe = models.IntegerField(db_column='Bit_scroe', blank=True, null=True)  # Field name made lowercase.
    pocket_id = models.CharField(db_column='Pocket_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    protein_name = models.CharField(db_column='Protein_name', max_length=256, blank=True, null=True)  # Field name made lowercase.
    n = models.CharField(max_length=128, blank=True, null=True)
    taxonomy = models.CharField(db_column='Taxonomy', max_length=256, blank=True, null=True)  # Field name made lowercase.
    taxid = models.CharField(db_column='TaxID', max_length=128, blank=True, null=True)  # Field name made lowercase.
    repid = models.CharField(db_column='RepID', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MMseqs2_rice'


class Mmseqs2Soybean(models.Model):
    target = models.CharField(db_column='Target', max_length=50, blank=True, null=True)  # Field name made lowercase.
    query = models.CharField(db_column='Query', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sequence_identity = models.FloatField(db_column='Sequence_identity', blank=True, null=True)  # Field name made lowercase.
    alignment_length = models.IntegerField(db_column='Alignment_length', blank=True, null=True)  # Field name made lowercase.
    number_of_mismatches = models.IntegerField(db_column='Number_of_mismatches', blank=True, null=True)  # Field name made lowercase.
    number_of_gap_openings = models.IntegerField(db_column='Number_of_gap_openings', blank=True, null=True)  # Field name made lowercase.
    start_position_in_query = models.IntegerField(db_column='Start_position_in_query', blank=True, null=True)  # Field name made lowercase.
    end_position_in_query = models.IntegerField(db_column='End_position_in_query', blank=True, null=True)  # Field name made lowercase.
    start_position_in_target = models.IntegerField(db_column='Start_position_in_target', blank=True, null=True)  # Field name made lowercase.
    end_position_in_target = models.IntegerField(db_column='End_position_in_target', blank=True, null=True)  # Field name made lowercase.
    evalue = models.FloatField(db_column='Evalue', blank=True, null=True)  # Field name made lowercase.
    bit_scroe = models.IntegerField(db_column='Bit_scroe', blank=True, null=True)  # Field name made lowercase.
    pocket_id = models.CharField(db_column='Pocket_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    protein_name = models.CharField(db_column='Protein_name', max_length=256, blank=True, null=True)  # Field name made lowercase.
    n = models.CharField(max_length=128, blank=True, null=True)
    taxonomy = models.CharField(db_column='Taxonomy', max_length=256, blank=True, null=True)  # Field name made lowercase.
    taxid = models.CharField(db_column='TaxID', max_length=128, blank=True, null=True)  # Field name made lowercase.
    repid = models.CharField(db_column='RepID', max_length=256, blank=True, null=True)  # Field name made lowercase.
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'MMseqs2_soybean'


class MmseqsArabidopsis(models.Model):
    query = models.CharField(max_length=50, blank=True, null=True)
    target = models.CharField(max_length=50, blank=True, null=True)
    sequence_identity = models.FloatField(blank=True, null=True)
    alignment_length = models.IntegerField(blank=True, null=True)
    number_of_mismatches = models.IntegerField(blank=True, null=True)
    number_of_gap_openings = models.IntegerField(blank=True, null=True)
    start_position_in_qurey = models.IntegerField(blank=True, null=True)
    end_position_in_query = models.IntegerField(blank=True, null=True)
    start_position_in_target = models.IntegerField(blank=True, null=True)
    end_position_in_target = models.IntegerField(blank=True, null=True)
    e_value = models.FloatField(db_column='E_value', blank=True, null=True)  # Field name made lowercase.
    bit_score = models.IntegerField(blank=True, null=True)
    pocket_id = models.CharField(db_column='Pocket_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=50, blank=True, null=True)  # Field name made lowercase.
    protein_names = models.CharField(db_column='Protein_names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    gene_names = models.CharField(db_column='Gene_names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    organism = models.CharField(db_column='Organism', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subcellular = models.CharField(db_column='Subcellular', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    doi_id = models.CharField(db_column='DOI_ID', max_length=4096, blank=True, null=True)  # Field name made lowercase.
    pdb = models.CharField(db_column='PDB', max_length=256, blank=True, null=True)  # Field name made lowercase.
    string = models.CharField(db_column='STRING', max_length=50, blank=True, null=True)  # Field name made lowercase.
    function_cc = models.CharField(db_column='Function_CC', max_length=8192, blank=True, null=True)  # Field name made lowercase.
    bindingdb = models.CharField(db_column='BindingDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orthodb = models.CharField(db_column='OrthoDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    expressionatlas = models.CharField(db_column='ExpressionAtlas', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MMseqs_arabidopsis'


class MmseqsMaize(models.Model):
    query = models.CharField(max_length=50, blank=True, null=True)
    target = models.CharField(max_length=50, blank=True, null=True)
    sequence_identity = models.FloatField(blank=True, null=True)
    alignment_length = models.IntegerField(blank=True, null=True)
    number_of_mismatches = models.IntegerField(blank=True, null=True)
    number_of_gap_openings = models.IntegerField(blank=True, null=True)
    start_position_in_qurey = models.IntegerField(blank=True, null=True)
    end_position_in_query = models.IntegerField(blank=True, null=True)
    start_position_in_target = models.IntegerField(blank=True, null=True)
    end_position_in_target = models.IntegerField(blank=True, null=True)
    e_value = models.FloatField(db_column='E_value', blank=True, null=True)  # Field name made lowercase.
    bit_score = models.IntegerField(blank=True, null=True)
    pocket_id = models.CharField(db_column='Pocket_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=50, blank=True, null=True)  # Field name made lowercase.
    protein_names = models.CharField(db_column='Protein_names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    gene_names = models.CharField(db_column='Gene_names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    subcellular = models.CharField(db_column='Subcellular', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    doi_id = models.CharField(db_column='DOI_ID', max_length=4096, blank=True, null=True)  # Field name made lowercase.
    pdb = models.CharField(db_column='PDB', max_length=256, blank=True, null=True)  # Field name made lowercase.
    string = models.CharField(db_column='STRING', max_length=50, blank=True, null=True)  # Field name made lowercase.
    function_cc = models.CharField(db_column='Function_CC', max_length=8192, blank=True, null=True)  # Field name made lowercase.
    organism = models.CharField(db_column='Organism', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bindingdb = models.CharField(db_column='BindingDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orthodb = models.CharField(db_column='OrthoDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    expressionatlas = models.CharField(db_column='ExpressionAtlas', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MMseqs_maize'


class MmseqsRice(models.Model):
    query = models.CharField(max_length=50, blank=True, null=True)
    target = models.CharField(max_length=50, blank=True, null=True)
    sequence_identity = models.FloatField(blank=True, null=True)
    alignment_length = models.IntegerField(blank=True, null=True)
    number_of_mismatches = models.IntegerField(blank=True, null=True)
    number_of_gap_openings = models.IntegerField(blank=True, null=True)
    start_position_in_qurey = models.IntegerField(blank=True, null=True)
    end_position_in_query = models.IntegerField(blank=True, null=True)
    start_position_in_target = models.IntegerField(blank=True, null=True)
    end_position_in_target = models.IntegerField(blank=True, null=True)
    e_value = models.FloatField(db_column='E_value', blank=True, null=True)  # Field name made lowercase.
    bit_score = models.IntegerField(blank=True, null=True)
    pocket_id = models.CharField(db_column='Pocket_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=50, blank=True, null=True)  # Field name made lowercase.
    protein_names = models.CharField(db_column='Protein_names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    gene_names = models.CharField(db_column='Gene_names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    organism = models.CharField(db_column='Organism', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subcellular = models.CharField(db_column='Subcellular', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    doi_id = models.CharField(db_column='DOI_ID', max_length=4096, blank=True, null=True)  # Field name made lowercase.
    pdb = models.CharField(db_column='PDB', max_length=256, blank=True, null=True)  # Field name made lowercase.
    string = models.CharField(db_column='STRING', max_length=50, blank=True, null=True)  # Field name made lowercase.
    function_cc = models.CharField(db_column='Function_CC', max_length=8192, blank=True, null=True)  # Field name made lowercase.
    bindingdb = models.CharField(db_column='BindingDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orthodb = models.CharField(db_column='OrthoDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    expressionatlas = models.CharField(db_column='ExpressionAtlas', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MMseqs_rice'


class MmseqsSoybean(models.Model):
    query = models.CharField(max_length=50, blank=True, null=True)
    target = models.CharField(max_length=50, blank=True, null=True)
    sequence_identity = models.FloatField(blank=True, null=True)
    alignment_length = models.IntegerField(blank=True, null=True)
    number_of_mismatches = models.IntegerField(blank=True, null=True)
    number_of_gap_openings = models.IntegerField(blank=True, null=True)
    start_position_in_qurey = models.IntegerField(blank=True, null=True)
    end_position_in_query = models.IntegerField(blank=True, null=True)
    start_position_in_target = models.IntegerField(blank=True, null=True)
    end_position_in_target = models.IntegerField(blank=True, null=True)
    e_value = models.FloatField(db_column='E_value', blank=True, null=True)  # Field name made lowercase.
    bit_score = models.IntegerField(blank=True, null=True)
    pocket_id = models.CharField(db_column='Pocket_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=50, blank=True, null=True)  # Field name made lowercase.
    protein_names = models.CharField(db_column='Protein_names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    gene_names = models.CharField(db_column='Gene_names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    organism = models.CharField(db_column='Organism', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subcellular = models.CharField(db_column='Subcellular', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    doi_id = models.CharField(db_column='DOI_ID', max_length=4096, blank=True, null=True)  # Field name made lowercase.
    pdb = models.CharField(db_column='PDB', max_length=256, blank=True, null=True)  # Field name made lowercase.
    string = models.CharField(db_column='STRING', max_length=50, blank=True, null=True)  # Field name made lowercase.
    function_cc = models.CharField(db_column='Function_CC', max_length=8192, blank=True, null=True)  # Field name made lowercase.
    bindingdb = models.CharField(db_column='BindingDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orthodb = models.CharField(db_column='OrthoDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    expressionatlas = models.CharField(db_column='ExpressionAtlas', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MMseqs_soybean'

