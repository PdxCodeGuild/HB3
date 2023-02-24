from django.urls import path

# Import the home view
from .views import home_view

appname = "url_short"

urlpatterns = [path("", home_view, name="home")]