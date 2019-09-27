from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
     template = loader.get_template('eplus_main/index.html')
     return render(request, 'eplus_main/index.html')
