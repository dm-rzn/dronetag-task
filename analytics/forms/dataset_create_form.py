# forms
from django import forms

# models
from analytics.models import FlightAnalyticsDataset


class DatasetCreateForm(forms.ModelForm):

    class Meta:
        model = FlightAnalyticsDataset
        fields = ['name', 'created_by']
