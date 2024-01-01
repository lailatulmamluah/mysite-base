from django import forms

from .models import kategori

class FromPondok( forms.Form):
    kategori = forms.ModelChoiceField(queryset=kategori.objects.all())
    nama_Santri = forms.CharField(max_length=100)
    alamat = forms.CharField(max_length=100)
    tgl_lahir = forms.DateField() 