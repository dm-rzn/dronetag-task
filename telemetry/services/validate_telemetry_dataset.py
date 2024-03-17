# services
from utils.data_import.services import validate_dataset

# resources
from telemetry.resources import TelemetryDatapointResource

# typing
from django.core.files.base import File
from users.models import User


def validate_telemetry_dataset(file: File, user: User):
    '''
    :raises: ReaderExcpetion
    :raises: ValidatorException
    '''
    validate_dataset(file, user, TelemetryDatapointResource)
