from django.urls import path
from . import views
app_name = 'app'

urlpatterns = [
    path('register/', views.user_registration, name='register'),
    path('reset/', views.reset_password, name='reset'),
    path('profile/', views.user_profile, name='profile'),
    path('login/', views.user_login, name='login'),
    path('signout/', views.signout_view, name='sign_out'),
]