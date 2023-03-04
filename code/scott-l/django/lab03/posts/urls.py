from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('',views.postsIndex,name='postsIndex'),
    path('public_profile/',views.user_post, name='user_post'),
]