from .csv_file_reader import CSVFileReader

# typing
from django.core.files.uploadedfile import TemporaryUploadedFile


class CSVTemporaryUploadedFileReader(CSVFileReader):
    def __init__(self, file: TemporaryUploadedFile):
        self.path = file.temporary_file_path()
