from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    ACTIVE = 'AC'
    IN_PROGRESS = 'PG'
    READY = 'RD'
    CLOSED = 'CL'
    OPEN = 'OP'
    STATUS_OF_TASK = [
        (ACTIVE, 'Active'),
        (IN_PROGRESS, 'In_Progress'),
        (READY, 'Ready'),
        (CLOSED, 'Closed'),
        (OPEN, 'Open'),
    ]
    title = models.CharField(max_length=255)
    exercise = models.CharField(max_length=255)
    author = models.ForeignKey(User, verbose_name='Author', related_name='author', on_delete=models.CASCADE)
    executor = models.ForeignKey(User, verbose_name='Executor', related_name='executor', on_delete=models.CASCADE)
    status = models.CharField(max_length=30, choices=STATUS_OF_TASK, default=STATUS_OF_TASK[0])

    def __str__(self):
        return self.title
