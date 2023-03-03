from django.urls import path

from . import views
app_name = "gl"
urlpatterns = [
    path('', views.index, name='index'),
    path('remove/<int:id>', views.remove_item, name='grocery_remove'),
    path('complete/<int:id>', views.complete_item, name='grocery_complete'),
]