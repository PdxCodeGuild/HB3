from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "ToDo"

urlpatterns = [
    path("", views.index, name="home"),
    # path('detail/<str:todo_id>', views.detail, name="detail"),
    # path("submit/", views.formSubmit, name="submit"),
    # path("fruits/", views.fruits, name="fruits"),
    # path("items/", views.todo_items, name="todo"),
    # path("json_response/", views.json_response, name="json"),
    # path("redirect/", views.url_redirect, name="redirect"),
    path('show', views.show_todo, name='show'),
    path('save', views.save_todo, name='save'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)