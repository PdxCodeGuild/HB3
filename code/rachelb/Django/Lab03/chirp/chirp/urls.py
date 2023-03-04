from django.contrib import admin
from django.urls import path, include
from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.user, name="Homepage"),
    path('user_login/', views.user_login, name="Login"),
    path('post/', include('posts.urls')),
]
