from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name="items"),
    path('Edit/<int:pk>/', views.Edit, name="Edit"),
    path('Delete/<int:pk>/', views.Delete, name="Delete"),
]