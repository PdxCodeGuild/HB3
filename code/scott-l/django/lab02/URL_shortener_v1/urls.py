from django.urls import path
from . import views

app_name = 'URL_shortener_v1'

urlpatterns = [
    path('', views.index, name='index')
]