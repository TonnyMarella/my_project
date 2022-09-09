# Generated by Django 4.1.1 on 2022-09-09 08:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_task_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-created_at', '-modified_at']},
        ),
        migrations.RemoveField(
            model_name='task',
            name='status',
        ),
        migrations.AddField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Дата створення'),
        ),
        migrations.AddField(
            model_name='task',
            name='modified_at',
            field=models.DateTimeField(auto_now=True, help_text='Дата останнього редагування'),
        ),
    ]