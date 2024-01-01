from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from .models import kategori, Pondok
from .forms import FromPondok
from django.views.decorators.csrf import csrf_exempt

def members(request):
  data = kategori.objects.all()
  context = {
    "judul": "",
    "sub judul": "",
    "kategori": data,
  }
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render(context, request))
 

def pondok(request):
  data_pondok = Pondok.objects.all().values()
  context = {
    "judul": "",
    "sub judul": "",
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

def program(request) :
    template = loader.get_template('program.html') 
    return HttpResponse(template.render())


def home(request) :
    template = loader.get_template('home.html') 
    return HttpResponse(template.render())

@csrf_exempt
def list(request):
   submitted = False
   if request.method == "POST":
      forms = FromPondok(request.POST)
      if forms.is_Valid():
         simpanData = Pondok.objects.create(
            kategori = forms.cleaned_data.get("kategori"),
            nama_santri = forms.cleaned_data.get("nama_santri"),
            alamat = forms.cleaned_data.get("alamat"),
            tgl_lahir = forms.cleaned_data.get("tgl_lahir"),
         )
         simpanData.save()
         return HttpResponseRedirect("/list?submitted=True")
   else:
     forms = FromPondok
     if "submitted" in request.GET:
        submitted = True
   context = {
      "forms": FromPondok,
   }
   template = loader.get_template('list.html')
   return HttpResponse(template.render())






