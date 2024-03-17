# services
from utils.data_import.services import (
    create_reader,
    create_validator,
)

# resources
from import_export import resources

# typing
from django.core.files.base import File
from users.models import User


def validate_dataset(file: File, user: User, resource: resources.Resource):
    '''
    :raises: ReaderExcpetion
    :raises: ValidatorException
    '''
    reader = create_reader(file)
    validator = create_validator(reader=reader, user=user, resource=resource)

    validator.validate()
