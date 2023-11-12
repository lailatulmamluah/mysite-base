from django.http import HttpResponse
from django.template import loader

def members(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())
def produk(request):
  template = loader.get_template('produk.html')
  return HttpResponse(template.render())

def aku(request):
    template = loader.get_template('aku.html')
    return HttpResponse(template.render())
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
   