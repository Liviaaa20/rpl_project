from django.urls import path
from . import views
from django.views.generic import RedirectView


urlpatterns = [
    path('', RedirectView.as_view(url='daftar/')),
    path('daftar/', views.daftar_mahasiswa, name='daftar_mahasiswa'),
    path('tambah/', views.tambah_mahasiswa, name='tambah_mahasiswa'),
    path('edit/<int:pk>/', views.edit_mahasiswa, name='edit_mahasiswa'),
    path('hapus/<int:pk>/', views.hapus_mahasiswa, name='hapus_mahasiswa'),
]