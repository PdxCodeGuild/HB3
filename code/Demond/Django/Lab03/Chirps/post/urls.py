from django.contrib.auth import views as auth_views
from django.urls import path
from .views import *

app_name = "post"
urlpatterns = [
    # path('', HomeView.as_view(), name='home'),
    path('chirp/', post_tweet, name='post')
    #the name of this path is to correlate.. refer to line 39 on html ,
]