from django.contrib import admin
from .models import Pondok, kategori

# Register your models here.


class pondokAdmin(admin.ModelAdmin):
    list_display = ("namapondok", "harga")

    
admin.site.register(kategori)
admin.site.register(Pondok , pondokAdmin)