# forms
from django import forms

# validators
from django.core.validators import FileExtensionValidator

# models
from analytics.models import FlightAnalyticsDataset


class DatasetCreateForm(forms.ModelForm):
    telemetry_data = forms.FileField(
        label='telemetry',
        validators=[FileExtensionValidator(['csv'])],
        required=True
    )
    status_data = forms.FileField(
        label='status',
        validators=[FileExtensionValidator(['csv'])],
        required=True,
    )

    class Meta:
        model = FlightAnalyticsDataset
        fields = ['name', 'created_by', 'telemetry_data', 'status_data']
