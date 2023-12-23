from django.http import HttpResponse
from django.template import loader
from .models import kategori, produk

def members(request):
  data = kategori.objects.all()
  context = {
    "judul": "Selamat datang di tempat makan",
    "sub judul": "Bakso bejo",
    "kategori": data,
  }
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render(context, request))
 

def produk(request):
  data_produk = produk.objects.all().values()
  context = {
    "judul": "Selamat datang di tempat makan",
    "sub judul": "Bakso bejo",
    "data": data,
  }
  template = loader.get_template('produk.html')
  return HttpResponse(template.render())

def detail_produk(request, id):
   data_produk = produk.objects.get(id=id)
   template = loader.get_template('detailproduk.html')
   context = {
      "produk": produk,
   }
   return HttpResponse(template.render(context, request))

def aku(request):
    template = loader.get_template('aku.html')
    return HttpResponse(template.render())

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
  