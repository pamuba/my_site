from django.http import HttpResponse
from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def simple_view(request):
    return HttpResponse("SIMPLE VIEW") #JINJA  html template  