from rest_framework.routers import SimpleRouter
from django.urls import path, include
from api import views

router = SimpleRouter()
router.register(r'task', views.TaskViewSet, basename='tasks')
router.register(r'my_task', views.TaskUserViewSet, basename='my_task')
urlpatterns = router.urls

urlpatterns += [
    path('api/v1/drf-auth/', include('rest_framework.urls')),
]