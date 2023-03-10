from django.urls import path
from .views import create_post, post_details

app_name = 'post'

urlpatterns = [
    path('create_post/', create_post, name='create'),
    path('<int:id>', post_details, name='details'),
]