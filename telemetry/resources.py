# django-import-export
from import_export import resources
from import_export.fields import Field

# widgets
from utils.data_import.widgets import DateTimeUtilWidget

# services
from telemetry.services import create_dry_import_dataset

# model
from .models import (
    TelemetryDatapoint,
)


class TelemetryDatapointResource(resources.ModelResource):
    # let's be explicit about every single field
    external_id = Field(attribute='external_id', column_name='id')
    time = Field(attribute='time', column_name='time', widget=DateTimeUtilWidget())
    time_received = Field(attribute='time_received', column_name='time_received', widget=DateTimeUtilWidget())
    latitude = Field(attribute='latitude', column_name='latitude')
    longitude = Field(attribute='longitude', column_name='longitude')
    altitude_m = Field(attribute='altitude_m', column_name='altitude')
    geo_altitude_m = Field(attribute='geo_altitude_m', column_name='geo_altitude')
    height_m = Field(attribute='height_m', column_name='height')
    velocity_x_ms = Field(attribute='velocity_x_ms', column_name='velocity_x')
    velocity_y_ms = Field(attribute='velocity_y_ms', column_name='velocity_y')
    velocity_z_ms = Field(attribute='velocity_z_ms', column_name='velocity_z')
    vertical_accuracy_m = Field(attribute='vertical_accuracy_m', column_name='vertical_accuracy')
    horizontal_accuracy_m = Field(attribute='horizontal_accuracy_m', column_name='horizontal_accuracy')
    velocity_accuracy_ms = Field(attribute='velocity_accuracy_ms', column_name='speed_accuracy')
    pressure_hpa = Field(attribute='pressure_hpa', column_name='pressure')

    class Meta:
        model = TelemetryDatapoint
        exclude = ['dataset']

    def __init__(self, dataset=None):
        super().__init__()
        self.dataset = dataset

    def before_import(self, dataset, using_transactions, dry_run, **kwargs):
        # for dry run it is necessary to create dataset for the validation to pass
        if dry_run and self.dataset is None:
            self.dataset = create_dry_import_dataset()

    def before_save_instance(self, instance, using_transactions, dry_run):
        instance.dataset = self.dataset
