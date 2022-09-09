from django.urls import path, include
from api import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'task', views.TaskViewSet, basename='tasks')
router.register(r'my_task', views.TaskUserViewSet, basename='my_task')

urlpatterns = [
    path('api/', include(router.urls)),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login/', views.LoginUser.as_view(), name='login')
]
