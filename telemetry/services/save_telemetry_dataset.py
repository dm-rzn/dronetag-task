# models
from telemetry.models import TelemetryDataset

# resources
from telemetry.resources import TelemetryDatapointResource

# services
from utils.data_import.services import save_dataset

# typing
from django.core.files.base import File
from users.models import User


def save_telemetry_dataset(name: str, file: File, user: User) -> TelemetryDataset:
    '''
    :raises: ReaderExcpetion
    :raises: LoaderException
    '''
    dataset = TelemetryDataset.objects.create(
        name=name,
        data=file,
        created_by=user,
    )

    return save_dataset(dataset, TelemetryDatapointResource)
