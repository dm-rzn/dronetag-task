from utils.data_import.abstract import AbstractReader

# exceptions
from utils.data_import.exceptions import ReaderException

# typing
from tablib import Dataset
from django.core.files.base import File


class TelemetryCSVFileReader(AbstractReader):
    def __init__(self, file: File):
        self.path = file.path

    def read(self) -> Dataset:
        try:
            with open(self.path, 'r') as f:
                return Dataset().load(f, headers=True)
        except Exception:
            raise ReaderException()
