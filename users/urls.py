from django.urls import path

from users import view

app_name = 'users'

urlpatterns = [
    path('register/', view.registration_view, name='register')
]