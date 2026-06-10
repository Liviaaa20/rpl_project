from django.urls import path
from . import views
from django.views.generic import RedirectView


urlpatterns = [
    path('', RedirectView.as_view(url='daftar/')),
    path('daftar/', views.daftar_mahasiswa, name='daftar_mahasiswa'),
]