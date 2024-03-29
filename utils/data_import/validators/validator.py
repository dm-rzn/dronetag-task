from utils.data_import.abstract.validator import AbstractValidator
from utils.data_import.abstract.reader import AbstractReader

# django-import-export
from import_export import resources

# exceptions
from utils.data_import.exceptions import (
    ReaderException,
    ValidatorException,
)

# typing
from users.models import User
from common.models import Dataset


class Validator(AbstractValidator):
    def __init__(self, reader: AbstractReader, dataset: Dataset, user: User, resource: resources.Resource):
        self.reader = reader
        self.dataset = dataset
        self.user = user
        self.resource = resource

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

        result = self.resource(self.user).import_data(data, dry_run=True)
        if result.has_errors() or result.has_validation_errors():
            # TODO: log
            raise ValidatorException()  # TODO: include errors, set code, ...
