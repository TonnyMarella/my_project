from django.urls import path

from users import view

urlpatterns = [
    path('register/', view.RegisterUserViewSet.as_view(), name='register')
]
