from utils.data_import.exceptions import (
    ReaderException,
    ValidatorException,
    LoaderException,
)


class StatusException(Exception):
    ...


class StatusReaderException(ReaderException, StatusException):
    ...


class StatusValidatorException(ValidatorException, StatusException):
    ...


class StatusLoaderException(LoaderException, StatusException):
    ...
