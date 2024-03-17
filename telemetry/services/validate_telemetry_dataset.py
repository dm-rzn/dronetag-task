# services
from utils.data_import.services import validate_dataset

# resources
from telemetry.resources import TelemetryDatapointResource

# exceptions
from utils.data_import.exceptions import (
    ReaderException,
    ValidatorException,
)
from telemetry.exceptions import (
    TelemetryReaderException,
    TelemetryValidatorException,
)

# typing
from django.core.files.base import File
from users.models import User


def validate_telemetry_dataset(file: File, user: User):
    '''
    :raises: TelemetryReaderExcpetion
    :raises: TelemetryValidatorException
    '''
    try:
        validate_dataset(file, user, TelemetryDatapointResource)
    except ReaderException:
        raise TelemetryReaderException()
    except ValidatorException:
        raise TelemetryValidatorException()
