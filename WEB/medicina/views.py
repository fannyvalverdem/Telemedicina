from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.template.context_processors import csrf 

# Create your views here.
@csrf_exempt 
def base(request):
  dictionary = dict(request=request) 
  dictionary.update(csrf(request)) 
  return render(request,'base.html', dictionary)