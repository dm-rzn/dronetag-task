from utils.data_import.abstract.loader import AbstractLoader
from utils.data_import.abstract.reader import AbstractReader

# django-import-export
from import_export import resources

# exceptions
from utils.data_import.exceptions import (
    ReaderException,
    LoaderException,
)

# typing
from common.models import Dataset


class Loader(AbstractLoader):
    def __init__(self, reader: AbstractReader, dataset: Dataset, resource: resources.Resource):
        self.reader = reader
        self.dataset = dataset
        self.resource = resource

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
            self.resource(dataset=self.dataset).import_data(data)
        except Exception:
            # TODO: log
            raise LoaderException()  # TODO: report
