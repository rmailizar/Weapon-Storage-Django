from django.db import models

class member(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    
class weapon(models.Model):
    nama = models.CharField(max_length=50)
    tipe = models.CharField(max_length=100)
    jumlah = models.IntegerField()
    
class RiwayatStok(models.Model):
    weapon = models.ForeignKey(weapon, on_delete=models.CASCADE)
    waktu = models.DateTimeField(auto_now_add=True)
    jumlah_perubahan = models.IntegerField()
    jenis_perubahan = models.CharField(max_length=10)