from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('details/<int:fish_id>/', views.fish_details, name='fish_details'),
]

#<int:fish_id>/