from django.urls import path
from . import views

app_name = 'urlshorter'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:code>/', views.redirect_url, name='redirect_url'),
]
