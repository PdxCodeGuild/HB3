from django.urls import path
from . import views

urlpatterns = [
    path('addChirp', views.addChirp, name="addChirp"),
    path('profileView', views.profileView, name="profileView")
]