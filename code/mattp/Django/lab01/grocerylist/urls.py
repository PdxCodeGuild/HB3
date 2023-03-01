from django.urls import path

from . import views
app_name = "gl"
urlpatterns = [
    path('add/', views.item_add, name='add'),
    path('delete/<int:id>', views.delete_item, name='delete'),
    path('completed/<int:id>', views.complete_item, name='complete'),
]