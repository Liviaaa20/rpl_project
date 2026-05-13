from urllib import request

from django.shortcuts import render
from django.http import HttpResponse
from .models import Mahasiswa



def index(request):
    """Simple HTTP response view."""
    return HttpResponse("Hello, ini modul praktikum RPL Django!")


def index_template(request):
    """Render index page with template and context data."""
    context = {
        'judul': 'Halo Mahasiswa',
        'deskripsi': 'Contoh halaman index menggunakan Django templates dan static files.'
    }
    return render(request, 'mahasiswa/index.html', context)

def daftar_mahasiswa(request):
    mahasiswas = Mahasiswa.objects.all()
    return render(request, 'mahasiswa/daftar.html', {'mahasiswas': mahasiswas})
