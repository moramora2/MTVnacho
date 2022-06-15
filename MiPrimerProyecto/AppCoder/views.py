from django.http import HttpResponse
from django.template import loader
from .models import Familia

def primera_vista(request):
  mydata = Familia.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'familias': mydata,
  }
  return HttpResponse(template.render(context, request))
    

    