from django.shortcuts import render

# Create your views here.
from .models import *

def home(request):
    query=Profile.objects.get(id=2)
    query2=Experience.objects.all()
    query3=Education.objects.all()
    query4=Skills.objects.all()
    query5=Interest.objects.all()
    query6=Awards.objects.all()
    context={
        'query':query,
        'query2':query2,
        'query3':query3,
        'query4':query4,
        'query5':query5,
        'query6':query6,
    }
    template_name='dam/resume/index.html'
    return render(request,template_name,context)