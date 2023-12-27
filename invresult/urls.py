from django.urls import path
from . import views

urlpatterns = [
    path('searchAPI/', views.searchAPI, name='searchAPI'),
    path('smile2pdb/', views.smile2pdb, name='smile2pdb'),
    path('searchPDBQT/', views.searchPDBQT, name='searchPDBQT'),
    path('searchDetail/', views.searchDetail, name='searchDetail'),
    path('searchMMseqs/', views.searchMMseqs, name='searchMMseqs'),
    path('searchFoldseek/', views.searchFoldseek, name='searchFoldseek')
]