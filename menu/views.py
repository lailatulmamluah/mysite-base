from django.http import HttpResponse
from django.template import loader
from .models import kategori, Pondok

def members(request):
  data = kategori.objects.all()
  context = {
    "judul": "Selamat datang di pondok pesantren",
    "sub judul": "Bustanul ulum sumber anom",
    "kategori": data,
  }
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render(context, request))
 

def produk(request):
  data_produk = Produk.objects.all().values()
  context = {
    "judul": "Selamat datang di pondok pesantren",
    "sub judul": "Bustanul ulum sumber anom",
    "data": data_produk,
  }
  template = loader.get_template('produk.html')
  return HttpResponse(template.render())

def detail_produk(request, id):
   data_produk = Produk.objects.get(id=id)
   template = loader.get_template('detailproduk.html')
   context = {
      "produk": data_produk,
   }
   return HttpResponse(template.render(context, request))

def aku(request):
    template = loader.get_template('aku.html')
    return HttpResponse(template.render())
  
def index(request) :
    template = loader.get_template('index.html') 
    return HttpResponse(template.render())

def contact(request) :
    template = loader.get_template('contact.html') 
    return HttpResponse(template.render())

def formulir(request) :
    template = loader.get_template('formulir.html') 
    return HttpResponse(template.render())


