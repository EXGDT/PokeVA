from django.shortcuts import render
from django.http import JsonResponse
import invresult.models
import invresult.serializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import LimitOffsetPagination

# Create your views here.

@api_view(['GET'])
def searchAPI(request):
    param = (request.GET.get('plant'), request.GET.get('cyto'))
    inv_database = {
        ('Arabidopsis', 'Abscisic_acid'): invresult.models.InvresultAbaAt,
    }
    query_result = inv_database.get(param).objects.all()
    if query_result is not None:
        paginator = LimitOffsetPagination()
        result_page = paginator.paginate_queryset(query_result, request)
        serializer = invresult.serializer.InvresultAbaAtSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    else:
        return Response({'error': 'No matching data found'}, status=404)
