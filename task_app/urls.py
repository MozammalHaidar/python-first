from django.urls import path
from .views import (
    task_list,
    create_task,
    edit_task,
    delete_task,
    toggle_task_status,
    dashboard,
)

urlpatterns = [
    path('tasks', task_list, name='task_list'),
    path('tasks/add/', create_task, name='create_task'),
    path('tasks/edit/<int:pk>/', edit_task, name='edit_task'),
    path('tasks/delete/<int:pk>/', delete_task, name='delete_task'),
    path('tasks/<int:pk>/toggle/', toggle_task_status, name='toggle_task_status'),
    path('dashboard/', dashboard, name='dashboard'),
]
