from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=255)
    exercise = models.CharField(max_length=255)
    author = models.ForeignKey(User, verbose_name='Author', related_name='author', on_delete=models.CASCADE)
    executor = models.ForeignKey(User, verbose_name='Executor', related_name='executor', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
