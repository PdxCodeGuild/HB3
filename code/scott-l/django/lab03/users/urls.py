from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.usersIndex,name='usersIndex'),
    path('register/', views.user_registration, name='user_registration'),
    path('reset/', views.user_reset_password, name='user_reset_password'),
    path('profile/', views.user_profile, name='user_profile'),
    path('login/', views.user_login, name='user_login'),
    path('signout/', views.user_signout, name='user_signout'),
]