from django.urls import path

from . import views
app_name = "gl"
urlpatterns = [
    path('', views.index, name='index'),
]