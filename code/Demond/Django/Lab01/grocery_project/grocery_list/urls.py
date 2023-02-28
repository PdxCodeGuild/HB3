from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('complete_item/<int:item_id>/', views.complete_item, name='complete_item'),
    path('delete_item/<int:item_id>/', views.delete_item, name='delete_item'),
]