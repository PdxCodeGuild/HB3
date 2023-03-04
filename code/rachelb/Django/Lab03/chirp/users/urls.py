from django.urls import path
from . import views 

urlpatterns = [
    path('home/', views.user, name="Homepage"),
    path('', views.user_login, name="Login")    
]