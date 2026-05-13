from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_template, name='index'),
    path('daftar/', views.daftar_mahasiswa, name='daftar_mahasiswa'),
]