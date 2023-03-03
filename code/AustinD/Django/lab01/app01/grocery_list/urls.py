from django.urls import path
from . import views

app_name = 'grocery_list'

urlpatterns = [
    path('', views.grocery_items, name='grocery_list'),
    path('add/', views.add_grocery_item, name='grocery_add'),
    path('remove/<int:id>', views.remove_grocery_item, name='grocery_remove'),
    path('complete/<int:id>', views.complete_grocery_item, name='grocery_complete'),
]