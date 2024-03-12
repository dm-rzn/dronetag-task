# forms
from django import forms

# models
from telemetry.models import TelemetryDataset

# services
from telemetry.services import (
    create_dry_import_dataset,
    create_reader,
    create_validator,
)

# exceptions
from django.core.exceptions import ValidationError
from utils.data_import.exceptions import (
    ReaderException,
    ValidatorException,
)


class TelemetryDatasetForm(forms.ModelForm):

    class Meta:
        model = TelemetryDataset
        fields = ['name', 'created_by', 'data']  # validate data as the last field

    def clean_data(self):
        data = self.cleaned_data['data']
        user = self.cleaned_data['created_by']

        reader = create_reader(data)
        fake_dataset = create_dry_import_dataset(user)
        validator = create_validator(reader=reader, dataset=fake_dataset)

        try:
            validator.validate()
        except (ReaderException, ValidatorException):
            raise ValidationError('TODO')  # TODO: set message and code
