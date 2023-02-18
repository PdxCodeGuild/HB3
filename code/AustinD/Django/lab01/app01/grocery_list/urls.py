from django.urls import path
from . import views

app_name = 'gl'

urlpatterns = [
    path('', views.grocery_items, name='grocery-list'),
    path('add/', views.add_grocery_item, name='grocery-add'),
    path('remove/<int:id>', views.remove_grocery_item, name='grocery-remove'),
    path('complete/<int:id>', views.complete_grocery_item, name='grocery-complete'),
]