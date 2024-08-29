from django.contrib import admin
from models.category import Category
from models.stack import Stack


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        # 'description',
    )


@admin.register(Stack)
class StackAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        # 'description',
    )

