from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('items/', views.TodoListView.as_view(), name='items'),
    path('items/<int:pk>/', views.TodoDetailView.as_view(), name='details'),
    path('items/create/', views.TodoCreate.as_view(), name='create'),
    path('items/<int:pk>/update', views.TodoUpdateView.as_view(), name='update'),
    path('items/<int:pk>/delete', views.TodoDeleteView.as_view(), name='delete'),
]