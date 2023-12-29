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
 

def pondok(request):
  data_pondok = Pondok.objects.all().values()
  context = {
    "judul": "Selamat datang di pondok pesantren",
    "sub judul": "Bustanul ulum sumber anom",
    "data": data_pondok,
  }
  template = loader.get_template('pondok.html')
  return HttpResponse(template.render())

def detail_pondok(request, id):
   data_pondok = Pondok.objects.get(id=id)
   template = loader.get_template('detailpondok.html')
   context = {
      "pondok": data_pondok,
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


