# admin
from django.contrib import admin


class ReadOnlyTabularInlineMixin(admin.TabularInline):
    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
