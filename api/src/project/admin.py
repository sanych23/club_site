from django.contrib import admin
from models.project import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'status', 
        'author_role', 
        'created_at', 
        'deadline', 
        'closed_at', 
        'author'
    )