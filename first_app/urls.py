from django.urls import path
from . import views


urlpatterns = [
    #localhost:8000/first_app/
    path('', views.simple_view)
]