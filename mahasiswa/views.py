from urllib import request

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
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

@login_required(login_url='/accounts/login/')
def daftar_mahasiswa(request):
    mahasiswas = Mahasiswa.objects.all()
    return render(request, 'mahasiswa/daftar.html', {'mahasiswas': mahasiswas})

@login_required(login_url='/accounts/login/')
def tambah_mahasiswa(request):
    """Create new mahasiswa"""
    if request.method == 'POST':
        nim = request.POST.get('nim')
        nama = request.POST.get('nama')
        programstudi = request.POST.get('programstudi')
        angkatan = request.POST.get('angkatan')
        
        # Validasi
        if nim and nama and programstudi and angkatan:
            # Check if nim already exists
            if Mahasiswa.objects.filter(nim=nim).exists():
                error = 'NIM sudah terdaftar!'
                return render(request, 'mahasiswa/form_mahasiswa.html', {'error': error})
            
            # Create new mahasiswa
            mahasiswa = Mahasiswa(
                nim=nim,
                nama=nama,
                programstudi=programstudi,
                angkatan=int(angkatan)
            )
            mahasiswa.save()
            return redirect('daftar_mahasiswa')
        else:
            error = 'Semua field harus diisi!'
            return render(request, 'mahasiswa/form_mahasiswa.html', {'error': error})
    
    return render(request, 'mahasiswa/form_mahasiswa.html')

@login_required(login_url='/accounts/login/')
def edit_mahasiswa(request, pk):
    """Update mahasiswa"""
    mahasiswa = get_object_or_404(Mahasiswa, pk=pk)
    
    if request.method == 'POST':
        mahasiswa.nim = request.POST.get('nim')
        mahasiswa.nama = request.POST.get('nama')
        mahasiswa.programstudi = request.POST.get('programstudi')
        mahasiswa.angkatan = int(request.POST.get('angkatan'))
        
        # Validasi
        if mahasiswa.nim and mahasiswa.nama and mahasiswa.programstudi and mahasiswa.angkatan:
            mahasiswa.save()
            return redirect('daftar_mahasiswa')
        else:
            error = 'Semua field harus diisi!'
            return render(request, 'mahasiswa/form_mahasiswa.html', {'error': error, 'mahasiswa': mahasiswa})
    
    return render(request, 'mahasiswa/form_mahasiswa.html', {'mahasiswa': mahasiswa})

@login_required(login_url='/accounts/login/')
def hapus_mahasiswa(request, pk):
    """Delete mahasiswa"""
    mahasiswa = get_object_or_404(Mahasiswa, pk=pk)
    
    if request.method == 'POST':
        mahasiswa.delete()
        return redirect('daftar_mahasiswa')
    
    return render(request, 'mahasiswa/konfirmasi_hapus.html', {'mahasiswa': mahasiswa})
