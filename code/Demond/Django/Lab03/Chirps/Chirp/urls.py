from django.contrib.auth import views as auth_views
from django.urls import path
from .views import *

app_name = "step1"

urlpatterns = [
    # path('', HomeView.as_view(), name='home'),
    path('login/', my_login, name='login'),
    path('logout/', my_logout, name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
]
# action="{% url 'step1:signup' %}" this is why it is important to have a unique app name in each url.py - this was in the html