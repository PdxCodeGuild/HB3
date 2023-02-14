from django.urls import path
from . import views
app_name='gl'
# URLConf
urlpatterns = [
    # path('hello/',views.say_hello)
    path('',views.grocery_items, name='grocery_list'),
    path('add/',views.add_grocery_item, name='grocery_add'),
    path('remove/<int:id>',views.remove_grocery_item, name='grocery_remove')
]