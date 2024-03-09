# admin
from django.contrib import admin

from common.admin import (
    ModelAdminFinalFieldsMixin,
    ReadOnlyTabularInlineMixin,
)

# models
from .models import (
    TelemetryDatapoint,
    TelemetryDataset,
)


class TelemetryDatapointInline(ReadOnlyTabularInlineMixin, admin.TabularInline):
    model = TelemetryDatapoint
    extra = 0
    ordering = ['time']


@admin.register(TelemetryDataset)
class TelemetryDatasetAdmin(ModelAdminFinalFieldsMixin, admin.ModelAdmin):
    list_display = ['name', 'created_by', 'created_at']
    fields = [
        'name',
        'data',
    ]
    search_fields = ['name']
    final_fields = ['data']

    inlines = [
        TelemetryDatapointInline,
    ]

    def save_model(self, request, obj, form, change):
        if obj.id is None:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)

    def get_inlines(self, request, obj):
        if obj is None:
            return []  # hide inline on create view
        else:
            return self.inlines
