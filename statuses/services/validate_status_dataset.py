# services
from utils.data_import.services import validate_dataset

# resources
from statuses.resources import StatusDatapointResource

# exeptions
from utils.data_import.exceptions import (
    ReaderException,
    ValidatorException,
)
from statuses.exceptions import (
    StatusReaderException,
    StatusValidatorException,
)

# typing
from django.core.files.base import File
from users.models import User


def validate_status_dataset(file: File, user: User):
    '''
    :raises: StatusReaderExcpetion
    :raises: StatusValidatorException
    '''
    try:
        validate_dataset(file, user, StatusDatapointResource)
    except ReaderException:
        raise StatusReaderException()
    except ValidatorException:
        raise StatusValidatorException()
