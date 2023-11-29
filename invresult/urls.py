from django.urls import path
from . import views

urlpatterns = [
    path('searchAPI/', views.searchAPI, name='searchAPI'),
]