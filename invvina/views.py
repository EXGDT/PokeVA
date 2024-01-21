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


def create_task(request):
    if request.method == 'POST':
        data = request.POST
        task = invresult.models.Task.objects.create(
            smiles_input=data.get('smilesInput'),
            protein_list=data.get('proteinList'),
            email_address=data.get('mailAddress'),
            plant=data.get('step2Plant'),
            status='pending'
        )
        return JsonResponse({'status': 'success', 'task_id': task.id})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

