from telemetry.data_import import (
    TelemetryCSVFileReader,
    TelemetryCSVTemporaryUploadedFileReader,
)

# typing
from utils.data_import.abstract.reader import AbstractReader

from django.core.files.uploadedfile import TemporaryUploadedFile


def create_reader(file) -> AbstractReader:
    # TODO: if multiple file upload handlers are introduced, this needs to conditionally create various readers
    # TODO: meh
    if isinstance(file, TemporaryUploadedFile):
        return TelemetryCSVTemporaryUploadedFileReader(file)
    else:
        return TelemetryCSVFileReader(file)
