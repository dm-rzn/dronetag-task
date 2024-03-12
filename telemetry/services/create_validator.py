from utils.data_import.validators import Validator

# resources
from telemetry.resources import TelemetryDatapointResource

# typing
from telemetry.models import TelemetryDataset
from users.models import User
from utils.data_import.abstract.reader import AbstractReader
from utils.data_import.abstract.validator import AbstractValidator


def create_validator(reader: AbstractReader, user: User, dataset: TelemetryDataset = None) -> AbstractValidator:
    # TODO: coupled with TelemetryValidator
    return Validator(reader=reader, user=user, dataset=dataset, resource=TelemetryDatapointResource)
