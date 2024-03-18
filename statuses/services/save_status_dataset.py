# models
from statuses.models import StatusDataset

# resources
from statuses.resources import StatusDatapointResource

# services
from utils.data_import.services import save_dataset

# exceptions
from utils.data_import.exceptions import (
    ReaderException,
    LoaderException,
)
from statuses.exceptions import (
    StatusReaderException,
    StatusLoaderException,
)

# typing
from django.core.files.base import File
from users.models import User


def save_status_dataset(name: str, file: File, user: User) -> StatusDataset:
    '''
    :raises: StatusReaderExcpetion
    :raises: StatusLoaderException
    '''
    dataset = StatusDataset.objects.create(
        name=name,
        data=file,
        created_by=user,
    )

    try:
        return save_dataset(dataset, StatusDatapointResource)
    except ReaderException:
        raise StatusReaderException()
    except LoaderException:
        raise StatusLoaderException()
