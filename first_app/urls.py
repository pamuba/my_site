from django.urls import path
from . import views

urlpatterns = [
    #localhost:8000/first_app/
    # path('', views.simple_view)


    #localhost:8000/first_app/sports/
    # path('sports/',views.sports_view),
    #localhost:8000/first_app/finance/
    # path('finance/', views.finance_view)

    path('<topic>/', views.news_views)
]