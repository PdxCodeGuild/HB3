from django.contrib import admin
from django.urls import path, include

from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.user_login, name="Login"),
    path('home/', views.user, name="Homepage"),
    path('post/', include('posts.urls')),
]
