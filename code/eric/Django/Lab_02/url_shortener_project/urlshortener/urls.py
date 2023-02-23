from django.urls import path

# Import the home view
from .views import home, redirect_url_view

appname = "shortener"

urlpatterns = [
    path("", home, name="home"),
    path('<str:shortened_part>', redirect_url_view, name='redirect'),
]