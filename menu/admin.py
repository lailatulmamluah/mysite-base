from django.contrib import admin
from .models import Produk, kategori

# Register your models here.


class produkAdmin(admin.ModelAdmin):
    list_display = ("namaproduk", "harga")

    
admin.site.register(kategori)
admin.site.register(Produk , produkAdmin)