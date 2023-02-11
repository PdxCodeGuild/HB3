from django.urls import path
from . import views

app_name = "myapp"

urlpatterns = [
    # localhost:8000/myapp
    path("", views.index, name="index"),
    # localhost:8000/myapp/about
    path("about/", views.about, name="about")
]