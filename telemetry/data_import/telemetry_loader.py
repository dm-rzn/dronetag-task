from utils.data_import.abstract.loader import AbstractLoader
from utils.data_import.abstract.reader import AbstractReader

# resource
from telemetry.resources import TelemetryDatapointResource

# exceptions
from utils.data_import.exceptions import (
    ReaderException,
    LoaderException,
)

# typing
import typing

if typing.TYPE_CHECKING:
    from telemetry.models import TelemetryDataset


class TelemetryLoader(AbstractLoader):
    def __init__(self, reader: AbstractReader, dataset: 'TelemetryDataset'):
        self.reader = reader
        self.dataset = dataset

    def load(self):
        '''
        :raises: ReaderException
        :raises: LoaderException
        '''
        try:
            data = self.reader.read()
        except ReaderException:
            # TODO: log
            raise  # explicit re-reaise TODO: or raise as ValidatorException?

        try:
            TelemetryDatapointResource(dataset=self.dataset).import_data(data)
        except Exception:
            # TODO: log
            raise LoaderException()  # TODO: report
