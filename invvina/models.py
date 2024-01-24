from django.db import models
import uuid

# Create your models here.

class InvvinaTask(models.Model):
    jobid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    smiles_input = models.CharField(max_length=1024)
    protein_list = models.TextField()
    plant = models.CharField(max_length=100)
    email_address = models.EmailField()
    status = models.CharField(max_length=50)


class InvvinaTaskReuslt(models.Model):
    smile = models.CharField(max_length=1024)
    plant = models.CharField(max_length=100)
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