# typing
from utils.data_import.abstract import (
    AbstractReader,
    AbstractValidator,
)


def validate_telemetry_data(file_path: str, reader: AbstractReader, validator: AbstractValidator) -> None:
    '''
    :raises: utils.data_import.exceptions.ReaderException
    :raises: utils.data_import.exceptions.ValidatorException
    '''
    dataset = reader.read(file_path)
    validator.validate(dataset)
