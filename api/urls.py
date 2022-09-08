from django.urls import path
from .views import TaskAPIList, TaskAPIUpdate, TaskForUserAPIList

urlpatterns = [
    path('api/task/', TaskAPIList.as_view(), name='task'),
    path('api/task/<int:pk>/', TaskAPIUpdate.as_view(), name='task_update'),
    path('api/my_task/', TaskForUserAPIList.as_view(), name='my_task'),
    path('api/my_task/<int:pk>/', TaskAPIUpdate.as_view(), name='my_task_update'),
]
