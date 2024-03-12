from .telemetry_csv_file_reader import TelemetryCSVFileReader

# typing
from django.core.files.uploadedfile import TemporaryUploadedFile


class TelemetryCSVTemporaryUploadedFileReader(TelemetryCSVFileReader):
    def __init__(self, file: TemporaryUploadedFile):
        self.path = file.temporary_file_path()
