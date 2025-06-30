from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Todo

@admin.register(Todo)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')     
    search_fields = ('title',)                
    list_filter = ('is_active',)              

