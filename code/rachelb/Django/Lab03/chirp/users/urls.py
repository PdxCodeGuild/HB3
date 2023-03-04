from django.urls import path
from . import views 

urlpatterns = [
    path('', views.user, name="Homepage"),
    path('user_login/', views.user_login, name="Login")
]