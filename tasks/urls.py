from django.urls import path
from .views import TaskListView, TaskDetailView

urlpatterns = [
    path("tasks/", TaskListView.as_view(), name="tasks"),
    path("task-detail/", TaskDetailView.as_view(), name="task-detail")
]
