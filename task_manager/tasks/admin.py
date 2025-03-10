from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date', 'status', 'is_completed')  # Show checkbox in admin
    readonly_fields = ('status',)  # Prevent direct edits to status

admin.site.register(Task, TaskAdmin)
