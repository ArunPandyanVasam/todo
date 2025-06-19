from django.contrib import admin
from .models import Task
#from todoApp.models import Task

# Register your models here.
# admin.site.register(Task) -> Defaulity functionalty

class TaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'is_completed', 'created_at', 'updated_at')
    list_filter = ('is_completed',)
    search_fields = ('task',) # their are alot of fields

admin.site.register(Task, TaskAdmin)


# Another way to override the functionality
# @admin.register(Task)
# class TaskAdmin(admin.ModelAdmin):
#     list_display = ('task', 'is_completed', 'created_at', 'updated_at')
#     list_filter = ('is_completed',)
#     search_fields = ('task',)
