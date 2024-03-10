from utils.data_import.abstract import AbstractReader

# exceptions
from utils.data_import.exceptions import ReaderException


from tablib import Dataset


class TelemetryCSVReader(AbstractReader):
    def read(self, file_path: str) -> Dataset:
        try:
            with open(file_path, 'r') as f:
                return Dataset().load(f, headers=True)
        except Exception:
            raise ReaderException()
