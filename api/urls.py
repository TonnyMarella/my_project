from django.urls import path, include
from api import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'task', views.TaskViewSet, basename='tasks')
router.register(r'my_task', views.TaskUserViewSet, basename='my_task')

urlpatterns = router.urls
