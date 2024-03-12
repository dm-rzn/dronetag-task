# services
from telemetry.services import (
    create_reader,
    create_loader,
)

# exceptions
from utils.data_import.exceptions import (
    ReaderException,
    LoaderException,
)

# typing
from users.models import User
from django.core.files.base import File
from telemetry.models import TelemetryDataset


def save_dataset(name: str, data: File, created_by: User) -> TelemetryDataset:
    # ^ avoiding passing form as parameter and saving the form
    dataset = TelemetryDataset.objects.create(
        name=name,
        data=data,
        created_by=created_by,
    )
    reader = create_reader(dataset.data)
    loader = create_loader(reader=reader, dataset=dataset)
    try:
        loader.load()
    except (ReaderException, LoaderException):
        # TODO: log
        ...  # TODO: handle

    return dataset
