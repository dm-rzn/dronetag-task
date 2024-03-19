# forms
from django import forms

# enum
from analytics.charts import ChartEnum


class DatasetDetailForm(forms.Form):
    chart = forms.TypedChoiceField(choices=ChartEnum.choices, required=False, coerce=int)

    def clean_chart(self):
        return self.cleaned_data['chart'] or ChartEnum.TELEMETRY_LATENCY
