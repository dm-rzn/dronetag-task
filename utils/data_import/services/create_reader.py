from utils.data_import.readers import (
    CSVFileReader,
    CSVTemporaryUploadedFileReader,
)

# typing
from utils.data_import.abstract.reader import AbstractReader

from django.core.files.uploadedfile import TemporaryUploadedFile


def create_reader(file) -> AbstractReader:
    # TODO: if multiple file upload handlers are introduced, this needs to conditionally create various readers
    # TODO: meh
    if isinstance(file, TemporaryUploadedFile):
        return CSVTemporaryUploadedFileReader(file)
    else:
        return CSVFileReader(file)
