from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('/index.html', views.index, name='index')
]