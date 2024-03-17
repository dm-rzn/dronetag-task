# models
from telemetry.models import TelemetryDataset

# resources
from telemetry.resources import TelemetryDatapointResource

# services
from utils.data_import.services import save_dataset

# exceptions
from utils.data_import.exceptions import (
    ReaderException,
    LoaderException,
)
from telemetry.exceptions import (
    TelemetryReaderException,
    TelemetryLoaderException,
)

# typing
from django.core.files.base import File
from users.models import User


def save_telemetry_dataset(name: str, file: File, user: User) -> TelemetryDataset:
    '''
    :raises: TelemetryReaderExcpetion
    :raises: TelemetryLoaderException
    '''
    dataset = TelemetryDataset.objects.create(
        name=name,
        data=file,
        created_by=user,
    )

    try:
        return save_dataset(dataset, TelemetryDatapointResource)
    except ReaderException:
        raise TelemetryReaderException()
    except LoaderException:
        raise TelemetryLoaderException()
