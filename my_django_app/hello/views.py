from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('Hello')
    #return render(request, 'hello/index.html')

# Create your views here.
