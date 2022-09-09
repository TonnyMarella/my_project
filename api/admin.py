from django.contrib import admin
from api.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'exercise', 'author', 'executor', 'status', 'created_at', 'modified_at')
    list_display_links = ('title',)
    search_fields = ('title', 'author', 'executor')
    list_editable = ('status',)
    list_filter = ('created_at', 'modified_at')
