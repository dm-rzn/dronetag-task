# admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# models
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin, admin.ModelAdmin):
    pass
