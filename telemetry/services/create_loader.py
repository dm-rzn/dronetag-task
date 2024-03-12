from telemetry.data_import import (
    TelemetryLoader,
)

# typing
from telemetry.models import TelemetryDataset
from utils.data_import.abstract.reader import AbstractReader
from utils.data_import.abstract.loader import AbstractLoader


def create_loader(reader: AbstractReader, dataset: TelemetryDataset) -> AbstractLoader:
    # TODO: coupled with TelemetryLoader
    return TelemetryLoader(reader, dataset)
