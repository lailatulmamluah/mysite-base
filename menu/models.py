from django.db import models
from django.contrib import admin

# Create your models here.
class kategori(models.Model):
    nama = models.CharField(max_length=100)

    
    def __str__(self):
        return f"{self.nama}"
    
# admin.site.register(kategori)

class Pondok(models.Model):
    kategori = models.ForeignKey(kategori, on_delete=models.CASCADE)
    namapondok = models.CharField(max_length=100)
    harga = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.namapondok} {self.harga}"
    
# admin.site.register(pondok)
