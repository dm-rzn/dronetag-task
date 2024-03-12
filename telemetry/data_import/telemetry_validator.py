from utils.data_import.abstract.validator import AbstractValidator
from utils.data_import.abstract.reader import AbstractReader

# resource
from telemetry.resources import TelemetryDatapointResource

# exceptions
from utils.data_import.exceptions import (
    ReaderException,
    ValidatorException,
)

# typing
import typing

from users.models import User
if typing.TYPE_CHECKING:
    from telemetry.models import TelemetryDataset


class TelemetryValidator(AbstractValidator):
    def __init__(self, reader: AbstractReader, dataset: 'TelemetryDataset', user: User):
        self.reader = reader
        self.dataset = dataset
        self.user = user

    def validate(self):
        '''
        :raises: ReaderException
        :raises: ValidatorException
        '''
        try:
            data = self.reader.read()
        except ReaderException:
            # TODO: log
            raise  # explicit re-reaise TODO: or raise as ValidatorException?

        result = TelemetryDatapointResource(self.user).import_data(data, dry_run=True)
        if result.has_errors() or result.has_validation_errors():
            # TODO: log
            raise ValidatorException()  # TODO: include errors, set code, ...
