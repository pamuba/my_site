from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
# def simple_view(request):
#     return HttpResponse("SIMPLE VIEW") #JINJA  html template  


articles = {
    'sports':'Sports Page',
    'finance':'Finance Page',
    'politics':'Politics Page'
}

def news_views(request, topic):
    return HttpResponse(articles[topic])

# def sports_view(request):
#     return HttpResponse(articles['sports']) #JINJA  html template  

# def finance_view(request):
#     return HttpResponse(articles['finance']) #JINJA  html template  
 