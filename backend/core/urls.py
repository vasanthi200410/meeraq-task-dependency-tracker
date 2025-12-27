from django.urls import path
from .views import create_task, list_tasks, update_status, add_dependency

urlpatterns = [
    path('tasks/', list_tasks),
    path('tasks/create/', create_task),
    path('tasks/<int:task_id>/status/', update_status),
    path('tasks/<int:task_id>/dependency/', add_dependency),
]
