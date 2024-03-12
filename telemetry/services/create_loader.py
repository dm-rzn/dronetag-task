from utils.data_import.loaders import Loader

# resources
from telemetry.resources import TelemetryDatapointResource

# typing
from telemetry.models import TelemetryDataset
from utils.data_import.abstract.reader import AbstractReader
from utils.data_import.abstract.loader import AbstractLoader


def create_loader(reader: AbstractReader, dataset: TelemetryDataset) -> AbstractLoader:
    # TODO: coupled with TelemetryLoader
    return Loader(reader=reader, dataset=dataset, resource=TelemetryDatapointResource)
