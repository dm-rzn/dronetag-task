# admin
from django.contrib import admin


class ModelAdminFinalFieldsMixin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)

        return [*self.final_fields, *readonly_fields] if obj else readonly_fields
