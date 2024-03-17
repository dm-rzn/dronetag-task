# models
from statuses.models import StatusDataset

# resources
from statuses.resources import StatusDatapointResource

# services
from utils.data_import.services import save_dataset

# typing
from django.core.files.base import File
from users.models import User


def save_status_dataset(name: str, file: File, user: User) -> StatusDataset:
    '''
    :raises: ReaderExcpetion
    :raises: LoaderException
    '''
    dataset = StatusDataset.objects.create(
        name=name,
        data=file,
        created_by=user,
    )

    return save_dataset(dataset, StatusDatapointResource)
