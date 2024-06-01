from django.shortcuts import redirect, render
from .models import weapon, RiwayatStok
from .forms import KurangiStokForm, TambahStokForm
from datetime import datetime

def index(request):
    wep=weapon.objects.all()
    return render(request, 'index.html',{'wep':wep})

def add(request):
    return render(request, 'add.html')

def addrec(request):
    x=request.POST['nama']
    y=request.POST['tipe']
    z=request.POST['jumlah']
    wep=weapon(nama=x,tipe=y,jumlah=z)
    wep.save()
    return redirect("/")
    
def delete(request,id):
    wep=weapon.objects.get(id=id)
    wep.delete()
    return redirect("/")

def update(request,id):
    wep=weapon.objects.get(id=id)
    return render(request,'update.html', {'wep':wep})

def uprec(request,id):
    x=request.POST['nama']
    y=request.POST['tipe']
    z=request.POST['jumlah']
    wep=weapon.objects.get(id=id)
    wep.nama=x
    wep.tipe=y
    wep.jumlah=z
    wep.save()
    return redirect("/")
    
def kurangi_stok(request, id):
    wep = weapon.objects.get(pk=id)
    if request.method == 'POST':
        try:
            jumlah_perubahan = int(request.POST['jumlah_perubahan'])
            if 0 < jumlah_perubahan <= wep.jumlah:
                wep.jumlah -= jumlah_perubahan
                wep.save()
                catat_riwayat_stok(wep, jumlah_perubahan, 'pengurangan')
                return redirect('/', weapon_id=id)
            else:
                # Handle case where jumlah_perubahan is not valid
                return render(request, 'kurangi_stok.html', {'wep': wep, 'error': 'Jumlah tidak valid'})
        except ValueError:
            # Handle case where jumlah_perubahan is not an integer
            return render(request, 'kurangi_stok.html', {'wep': wep, 'error': 'Jumlah harus berupa angka'})
    return render(request, 'kurang_stok.html', {'wep': wep})

def tambah_stok(request, id):
    wep = weapon.objects.get(pk=id)
    if request.method == 'POST':
        try:
            jumlah_perubahan = int(request.POST['jumlah_perubahan'])
            if jumlah_perubahan > 0:
                wep.jumlah += jumlah_perubahan
                wep.save()
                catat_riwayat_stok(wep, jumlah_perubahan, 'penambahan')
                return redirect('/', weapon_id=id)
            else:
                # Handle case where jumlah_perubahan is not a positive integer
                return render(request, 'tambah_stok.html', {'wep': wep, 'error': 'Jumlah harus lebih dari 0'})
        except ValueError:
            # Handle case where jumlah_perubahan is not an integer
            return render(request, 'tambah_stok.html', {'wep': wep, 'error': 'Jumlah harus berupa angka'})
    return render(request, 'tambah_stok.html', {'wep': wep})

def catat_riwayat_stok(wep, jumlah_perubahan, jenis_perubahan):
    riwayat = RiwayatStok(weapon=wep, jumlah_perubahan=jumlah_perubahan, jenis_perubahan=jenis_perubahan)
    riwayat.save()
    
def riwayat_stok(request):
    riwayat = RiwayatStok.objects.all().select_related('weapon')
    return render(request, 'riwayat_stok.html', {'riwayat': riwayat})