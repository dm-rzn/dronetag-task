from utils.data_import.exceptions import (
    ReaderException,
    ValidatorException,
    LoaderException,
)


class TelemetryException(Exception):
    ...


class TelemetryReaderException(ReaderException, TelemetryException):
    ...


class TelemetryValidatorException(ValidatorException, TelemetryException):
    ...


class TelemetryLoaderException(LoaderException, TelemetryException):
    ...
