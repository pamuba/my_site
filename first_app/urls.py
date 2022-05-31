from django.urls import path
from . import views

urlpatterns = [
    #localhost:8000/first_app/
    # path('', views.simple_view)


    #localhost:8000/first_app/sports/
    # path('sports/',views.sports_view),
    #localhost:8000/first_app/finance/
    # path('finance/', views.finance_view)

    path('<str:topic>/', views.news_views),
    path('<int:num1>/<int:num2>', views.add_view)
]