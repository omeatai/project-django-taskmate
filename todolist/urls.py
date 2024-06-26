from django.urls import path
from todolist import views

urlpatterns = [
    path('', views.home, name="home"),
    path('todolist/', views.todolist, name="todolist"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('edit/<int:id>', views.edit_task, name="edit-task"),
    path('delete/<int:id>', views.delete_task, name="delete-task"),
    path('completed/<int:id>', views.completed, name="completed"),
    path('pending/<int:id>', views.pending, name="pending"),
]
