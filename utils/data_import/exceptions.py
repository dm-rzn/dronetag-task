class DataImportException(Exception):
    ...


class ReaderException(DataImportException):
    ...


class ValidatorException(DataImportException):
    ...


class LoaderException(DataImportException):
    ...
