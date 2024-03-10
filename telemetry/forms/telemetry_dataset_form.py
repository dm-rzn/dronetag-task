# forms
from django import forms

# models
from telemetry.models import TelemetryDataset


class TelemetryDatasetForm(forms.ModelForm):

    class Meta:
        model = TelemetryDataset
        fields = ['name', 'data', 'created_by']
