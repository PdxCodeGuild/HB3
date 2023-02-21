from django.urls import path
from . import views

# connecting an apps urls.py to a view

app_name = 'URL_shortener_v1'

urlpatterns = [
    # localhost:8000/index/
    # path('', views.index, name='index'),
    # localhost:8000/myurl/short_URL
    path('short_URL/', views.URLsubmit, name='Input_myurl'),
    path('redirect_URL/', views.URLredirect, name='Redirect_the_url')
]