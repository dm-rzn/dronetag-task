# forms
from django import forms

# models
from statuses.models import StatusDataset

# services
from utils.data_import.services import (
    create_reader,
    create_validator,
)

# resources
from statuses.resources import StatusDatapointResource

# exceptions
from django.core.exceptions import ValidationError
from utils.data_import.exceptions import (
    ReaderException,
    ValidatorException,
)


class StatusDatasetForm(forms.ModelForm):

    class Meta:
        model = StatusDataset
        fields = ['name', 'created_by', 'data']  # validate data as the last field

    def clean_data(self):
        data = self.cleaned_data['data']
        user = self.cleaned_data['created_by']

        reader = create_reader(data)
        validator = create_validator(reader=reader, user=user, resource=StatusDatapointResource)

        try:
            validator.validate()
        except (ReaderException, ValidatorException):
            raise ValidationError('TODO')  # TODO: set message and code

        return data
