from django.urls import path

# Import the home view
from .views import home_view

appname = "app"

urlpatterns = [
    # Home view
    path("", home_view, name="home")
]