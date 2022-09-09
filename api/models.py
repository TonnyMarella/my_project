from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()


class DateTimesABC(models.Model):
    created_at = models.DateTimeField(default=timezone.now, help_text='Дата створення')
    modified_at = models.DateTimeField(auto_now=True, help_text='Дата останнього редагування')

    class Meta:
        abstract = True
        ordering = ['-created_at', '-modified_at']


class Task(DateTimesABC):
    class StatusTask(models.TextChoices):
        ACTIVE = 'AC'
        IN_PROGRESS = 'PG'
        READY = 'RD'
        CLOSED = 'CL'
        OPEN = 'OP'

    title = models.CharField(max_length=255)
    exercise = models.CharField(max_length=255)
    author = models.ForeignKey(User, verbose_name='Author', related_name='author', on_delete=models.CASCADE)
    executor = models.ForeignKey(User, verbose_name='Executor', related_name='executor', on_delete=models.CASCADE)
    status = models.CharField(choices=StatusTask.choices, max_length=50)

    def __str__(self):
        return self.title
