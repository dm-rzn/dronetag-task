from utils.data_import.abstract import AbstractValidator

# resource
from telemetry.resources import TelemetryDatapointResource

# exceptions
from utils.data_import.exceptions import ValidatorException

# typing
import typing
from tablib import Dataset

if typing.TYPE_CHECKING:
    from telemetry.models import TelemetryDataset


class TelemetryValidator(AbstractValidator):
    def __init__(self, dataset: 'TelemetryDataset') -> None:
        super().__init__()
        self.dataset = dataset

    def validate(self, data: Dataset) -> None:
        result = TelemetryDatapointResource(dataset=self.dataset).import_data(data, dry_run=True)
        if result.has_errors() or result.has_validation_errors():
            raise ValidatorException()  # TODO: include errors
