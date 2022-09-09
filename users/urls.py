from django.urls import path

from users import view

urlpatterns = [
    path('register/', view.RegisterUserAPIView.as_view(), name='register')
]
