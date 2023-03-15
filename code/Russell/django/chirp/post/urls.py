from django.urls import path
from . import views
from users.views import register

urlpatterns = [
    path('', views.index, name='index'),
    path('all_profiles/', views.all_profiles, name='all_profiles'),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', register, name='register')
]