from django.core.files.base import File
from django.core.files.storage import FileSystemStorage

# typing
from utils.data_import.abstract import (
    AbstractReader,
    AbstractValidator,
)

# services
from telemetry.services import validate_telemetry_data

# exceptions
from django.core.exceptions import ValidationError
from utils.data_import.exceptions import (
    ReaderException,
    ValidatorException,
)

# i18n
from django.utils.translation import gettext_lazy as _


def validate_uploaded_telemetry_data(file: File, reader: AbstractReader, validator: AbstractValidator):
    directory = '/tmp'
    storage = FileSystemStorage(location=directory)

    filename = storage.save(file.name, file)
    path = f'{directory}/{filename}'

    try:
        validate_telemetry_data(path, reader, validator)
    except ReaderException:
        # TODO: log
        raise ValidationError(_('File could not be read.'), code='dataset-read-failed')  # TODO
    except ValidatorException:
        # TODO: log
        raise ValidationError(_('Validation failed.'), code='dataset-invalid')  # TODO
    finally:
        # TODO: log
        storage.delete(filename)
