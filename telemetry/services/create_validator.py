from telemetry.data_import import (
    TelemetryValidator,
)

# typing
from telemetry.models import TelemetryDataset
from utils.data_import.abstract.reader import AbstractReader
from utils.data_import.abstract.validator import AbstractValidator


def create_validator(reader: AbstractReader, dataset: TelemetryDataset) -> AbstractValidator:
    return TelemetryValidator(reader=reader, dataset=dataset)
