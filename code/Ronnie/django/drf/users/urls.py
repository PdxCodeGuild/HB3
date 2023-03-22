from django.urls import path, include
from .views import profile, user_registration


app_name = "accounts"

urlpatterns = [
    path('profile/', profile, name="profile"),
    path('register/', user_registration, name="register"),
    path('accounts/', include("django.contrib.auth.urls")),
]