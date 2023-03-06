from django.contrib import admin
from django.urls import path, include

from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.user_login, name="Login"),
    path('home/', views.user_home, name="Homepage"),
    path('register/', views.register, name="Register"),
    path('post/', include('posts.urls')),
]
