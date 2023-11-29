from django.db import models

# Create your models here.

class InvresultAbaAt(models.Model):
    uniprot_id = models.CharField(db_column='Uniprot_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    protein_names = models.CharField(db_column='Protein_names', max_length=512, blank=True, null=True)  # Field name made lowercase.
    gene_names = models.CharField(db_column='Gene_Names', max_length=128, blank=True, null=True)  # Field name made lowercase.
    organism = models.CharField(db_column='Organism', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pdb = models.CharField(db_column='PDB', max_length=256, blank=True, null=True)  # Field name made lowercase.
    pocket_id = models.CharField(db_column='Pocket_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    binding_affinity = models.FloatField(db_column='Binding_affinity', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'InvResult_ABA_At'