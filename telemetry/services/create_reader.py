from telemetry.data_import import (
    TelemetryCSVTemporaryUploadedFileReader,
)

# typing
from utils.data_import.abstract.reader import AbstractReader


def create_reader(file) -> AbstractReader:
    # TODO: if multiple file upload handlers are introduced, this needs to conditionally create various readers
    return TelemetryCSVTemporaryUploadedFileReader(file)
