# forms
from django import forms


class DatasetListForm(forms.Form):
    page = forms.IntegerField(required=False)
    q = forms.CharField(required=False)
