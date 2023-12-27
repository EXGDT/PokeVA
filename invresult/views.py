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

# Create your views here.
inv_database = {
    # ('Arabidopsis', 'Abscisic_acid'): invresult.models.InvresultAbaAt,
    (
        "Arabidopsis",
        "Abscisic_acid",
    ): invresult.models.InvresultArabidopsisAbscisicAcid,
    ("Arabidopsis", "Auxin"): invresult.models.InvresultArabidopsisAuxin,
    (
        "Arabidopsis",
        "Brassinosteroid",
    ): invresult.models.InvresultArabidopsisBrassinolide,
    ("Arabidopsis", "Cytokinin"): invresult.models.InvresultArabidopsisCytokinin,
    ("Arabidopsis", "Ethylene"): invresult.models.InvresultArabidopsisEthylene,
    (
        "Arabidopsis",
        "Gibberellin",
    ): invresult.models.InvresultArabidopsisGibberellin,
    (
        "Arabidopsis",
        "Jasmonic_acid",
    ): invresult.models.InvresultArabidopsisJasmonate,
    (
        "Arabidopsis",
        "Salicylic_acid",
    ): invresult.models.InvresultArabidopsisSalicylicAcid,
    (
        "Arabidopsis",
        "Stringolactone",
    ): invresult.models.InvresultArabidopsisStrigolactone,
    ("Zea", "Abscisic_acid"): invresult.models.InvresultMaizeAbscisicAcid,
    ("Zea", "Auxin"): invresult.models.InvresultMaizeAuxin,
    ("Zea", "Cytokinin"): invresult.models.InvresultMaizeCytokinin,
    ("Zea", "Ethylene"): invresult.models.InvresultMaizeEthylene,
    ("Zea", "Gibberellin"): invresult.models.InvresultMaizeGibberellin,
    ("Zea", "Jasmonic_acid"): invresult.models.InvresultMaizeJasmonate,
    ("Zea", "Salicylic_acid"): invresult.models.InvresultMaizeSalicylicAcid,
    ("Zea", "Stringolactone"): invresult.models.InvresultMaizeStrigolactone,
    ("Oryza", "Abscisic_acid"): invresult.models.InvresultRiceAbscisicAcid,
    ("Oryza", "Auxin"): invresult.models.InvresultRiceAuxin,
    ("Oryza", "Brassinosteroid"): invresult.models.InvresultRiceBrassinolide,
    ("Oryza", "Cytokinin"): invresult.models.InvresultRiceCytokinin,
    ("Oryza", "Ethylene"): invresult.models.InvresultRiceEthylene,
    ("Oryza", "Gibberellin"): invresult.models.InvresultRiceGibberellin,
    ("Oryza", "Jasmonic_acid"): invresult.models.InvresultRiceJasmonate,
    ("Oryza", "Salicylic_acid"): invresult.models.InvresultRiceSalicylicAcid,
    ("Oryza", "Stringolactone"): invresult.models.InvresultRiceStrigolactone,
    ("Glycine", "Abscisic_acid"): invresult.models.InvresultSoybeanAbscisicAcid,
    ("Glycine", "Auxin"): invresult.models.InvresultSoybeanAuxin,
    ("Glycine", "Cytokinin"): invresult.models.InvresultSoybeanCytokinin,
    ("Glycine", "Ethylene"): invresult.models.InvresultSoybeanEthylene,
    ("Glycine", "Gibberellin"): invresult.models.InvresultSoybeanGibberellin,
    ("Glycine", "Jasmonic_acid"): invresult.models.InvresultSoybeanJasmonate,
    ("Glycine", "Salicylic_acid"): invresult.models.InvresultSoybeanSalicylicAcid,
    ("Glycine", "Stringolactone"): invresult.models.InvresultSoybeanStrigolactone,
}
mmseqs_database = {
    "Arabidopsis": invresult.models.Mmseqs2Arabidopsis,
    "Oryza": invresult.models.Mmseqs2Rice,
    "Glycine": invresult.models.Mmseqs2Soybean,
    "Zea": invresult.models.Mmseqs2Maize
}
foldseek_database = {
    "Arabidopsis": invresult.models.FoldseekArabidopsis,
    "Oryza": invresult.models.FoldseekRice,
    "Glycine": invresult.models.FoldseekSoybean,
    "Zea": invresult.models.FoldseekMaize
}


@api_view(["GET"])
def searchAPI(request):
    param = (request.GET.get("plant"), request.GET.get("cyto"))
    order_by_fields = request.GET.get("order_by", "").split(',')
    search_query = request.GET.get("search", "")
    filter_querys = request.GET.get("filter", "").split(',')
    query_result = inv_database.get(param).objects.all()
    if query_result is not None:
        if search_query:
            query_result = query_result.filter(
                Q(uniprot_id__icontains=search_query)
                | Q(pocket_id__icontains=search_query)
                | Q(afdb_id__icontains=search_query)
                | Q(binding_affinity__icontains=search_query)
                | Q(protein_names__icontains=search_query)
                | Q(gene_names__icontains=search_query)
                | Q(organism__icontains=search_query)
                | Q(subcellular_location__icontains=search_query)
                | Q(doi_id__icontains=search_query)
                | Q(pdb__icontains=search_query)
                | Q(string__icontains=search_query)
                | Q(function_description__icontains=search_query)
                | Q(bindingdb__icontains=search_query)
                | Q(orthodb__icontains=search_query)
                | Q(expressionatlas__icontains=search_query)
            )
        if filter_querys:
            filter_conditions = [Q(**{filter_query + "__isnull": False}) for filter_query in filter_querys if filter_query]
            filter_conditions += [Q(**{filter_query + "__gt": ''}) for filter_query in filter_querys if filter_query]
            query_result = query_result.filter(*filter_conditions)
            print(filter_conditions)

        if order_by_fields:
            order_by_fields = [field for field in order_by_fields if field]
            query_result = query_result.order_by(*order_by_fields)
        paginator = LimitOffsetPagination()
        result_page = paginator.paginate_queryset(query_result, request)
        serializer_class = type(
            "DynamicInvresultSerializer",
            (invresult.serializer.GenericInvresultSerializer,),
            {
                "Meta": type(
                    "Meta", (), {"model": inv_database[(param)], "fields": "__all__"}
                )
            },
        )
        # serializer = invresult.serializer.InvresultAbaAtSerializer(result_page, many=True)
        serializer = serializer_class(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    else:
        return Response({"error": "No matching data found"}, status=404)


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


@api_view(["GET"])
def searchPDBQT(request):
    param = (request.GET.get("plant"), request.GET.get("cyto"))
    pocket_id = request.GET.get("pocket_id")
    query_result = inv_database.get(param).objects.get(pocket_id=pocket_id)
    if query_result is not None:
        ligand_path = query_result.ligand_path
        receptor_path = query_result.receptor_path
        complex_path = query_result.complex_path
        detail = query_result
        with open(ligand_path, "r") as file:
            ligand_content = file.read()
        with open(receptor_path, "r") as file:
            receptor_content = file.read()
        with open(complex_path, 'r') as file:
            complex_content = file.read()
        return JsonResponse({"ligand_content": ligand_content, "receptor_content": receptor_content, "complex_content": complex_content})
    else:
        return Response({"error": "No matching data found"}, status=404)

@api_view(["GET"])
def searchDetail(request):
    param = (request.GET.get("plant"), request.GET.get("cyto"))
    pocket_id = request.GET.get("pocket_id")
    query_result = inv_database.get(param).objects.get(pocket_id=pocket_id)
    if query_result is not None:
        serializer_class = type(
            "DynamicInvresultSerializer",
            (invresult.serializer.GenericInvresultSerializer,),
            {
                "Meta": type(
                    "Meta", (), {"model": inv_database[(param)], "fields": "__all__"}
                )
            },
        )
        detail = serializer_class(query_result)
        return JsonResponse(detail.data, safe=False)
    else:
        return Response({"error": "No matching data found"}, status=404)

@api_view(["GET"])
def searchMMseqs(request):
    param = (request.GET.get("plant"))
    pocket_id = request.GET.get("pocket_id")
    order_by_fields = request.GET.get("order_by", "").split(',')
    search_query = request.GET.get("search", "")
    query_result = mmseqs_database.get(param).objects.filter(pocket_id=pocket_id)
    if query_result is not None:
        if search_query:
            query_result = query_result.filter(
                Q(target__icontains=search_query)
                | Q(query__icontains=search_query)
                | Q(protein_name__icontains=search_query)
                | Q(taxonomy__icontains=search_query)
                | Q(taxid__icontains=search_query)
                | Q(repid__icontains=search_query)
            )
        if order_by_fields:
            order_by_fields = [field for field in order_by_fields if field]
            query_result = query_result.order_by(*order_by_fields)
        paginator = LimitOffsetPagination()
        result_page = paginator.paginate_queryset(query_result, request)
        serializer_class = type(
            "DynamicInvresultSerializer",
            (invresult.serializer.GenericInvresultSerializer,),
            {
                "Meta": type(
                    "Meta", (), {"model": mmseqs_database[(param)], "fields": "__all__"}
                )
            },
        )
        serializer = serializer_class(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    else:
        return Response({"error": "No matching data found"}, status=404)

@api_view(["GET"])
def searchFoldseek(request):
    param = (request.GET.get("plant"))
    pocket_id = request.GET.get("pocket_id")
    order_by_fields = request.GET.get("order_by", "").split(',')
    search_query = request.GET.get("search", "")
    query_result = foldseek_database.get(param).objects.filter(pocket_id=pocket_id)
    if query_result is not None:
        if search_query:
            query_result = query_result.filter(
                Q(target__icontains=search_query)
                | Q(query__icontains=search_query)
                | Q(protein_name__icontains=search_query)
                | Q(taxonomy__icontains=search_query)
                | Q(taxid__icontains=search_query)
                | Q(repid__icontains=search_query)
            )
        if order_by_fields:
            order_by_fields = [field for field in order_by_fields if field]
            query_result = query_result.order_by(*order_by_fields)
        paginator = LimitOffsetPagination()
        result_page = paginator.paginate_queryset(query_result, request)
        serializer_class = type(
            "DynamicInvresultSerializer",
            (invresult.serializer.GenericInvresultSerializer,),
            {
                "Meta": type(
                    "Meta", (), {"model": foldseek_database[(param)], "fields": "__all__"}
                )
            },
        )
        serializer = serializer_class(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    else:
        return Response({"error": "No matching data found"}, status=404)