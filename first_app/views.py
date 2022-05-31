
from django.shortcuts import render
from django.http.response import HttpResponse,HttpResponseNotFound, Http404

# Create your views here.
# def simple_view(request):
#     return HttpResponse("SIMPLE VIEW") #JINJA  html template  


articles = {
    'sports':'Sports Page',
    'finance':'Finance Page',
    'politics':'Politics Page'
}

def news_views(request, topic):
    try:
        result = articles[topic]
        return HttpResponse(result)
    except:
        # result = "No Page for the topic!!"
        # return HttpResponseNotFound(result)
        raise Http404("404 GENERIC ERROR") #404.html


def add_view(request, num1, num2):
    #localhost:8000/first_app/num1/num2
    add_result = num1 + num2
    result = f'{num1}+{num2} = {add_result}'
    return HttpResponse(result)

# def sports_view(request):
#     return HttpResponse(articles['sports']) #JINJA  html template  

# def finance_view(request):
#     return HttpResponse(articles['finance']) #JINJA  html template  
 