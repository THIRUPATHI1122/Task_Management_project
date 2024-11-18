from django.urls import path
from .views import task_list,task_add, task_edit, task_delete, task_detail


urlpatterns = [
    path('', task_list, name='task_list'),
    path('task/task/add/', task_add, name='task_add'),
    path('task/task/<int:pk>/edit/', task_edit, name='task_edit'),
    path('task/task/<int:pk>/delete/', task_delete, name='task_delete'),
    path('task/task/<int:pk>/', task_detail, name='task_detail'),

]
