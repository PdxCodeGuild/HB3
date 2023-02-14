from django.urls import path
from . import views

app_name = "myapp"

urlpatterns = [
    path('', views.index, name='index'),
    path('add_item', views.add_item, name='add_item'),
    path('completed_item/<item_id>', views.completed_item, name='completed_item'),
    path('deleted_item/<item_id>', views.deleted_item, name='deleted_item'),
]
