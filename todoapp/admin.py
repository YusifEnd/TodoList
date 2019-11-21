from django.contrib import admin
from .models import Todo

# Register your models here.


class AdminModel(admin.ModelAdmin):
    list_display = ['title', 'created_date', 'due_date', 'completed']
    list_display_links = ['title', 'created_date', 'due_date']
    list_editable = ['completed']
    search_fields = ['title', 'content']


admin.site.register(Todo, AdminModel)
