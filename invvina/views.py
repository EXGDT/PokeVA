from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import JsonResponse
import invresult.models
import invresult.serializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import LimitOffsetPagination
from django.db.models import Q

from rdkit import Chem
from rdkit.Chem import AllChem

@api_view(["POST"])
def smile2pdb(request):
    smile = request.data.get("smile")

    def smiles_to_pdb(smile):
        molecule = Chem.MolFromSmiles(smile)
        molecule = Chem.AddHs(molecule)
        AllChem.EmbedMolecule(molecule, AllChem.ETKDG())
        pdb_block = Chem.MolToPDBBlock(molecule)
        return pdb_block

    pdb_data = smiles_to_pdb(smile)
    return Response({"pdb": pdb_data}, status=200)
