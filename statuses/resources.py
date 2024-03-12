# django-import-export
from import_export import resources
from import_export.fields import Field

# widgets
from utils.data_import.widgets import DateTimeUtilWidget

# services
from statuses.services import create_dry_import_dataset

# model
from .models import (
    StatusDatapoint,
)


class StatusDatapointResource(resources.ModelResource):
    # let's be explicit about every single field
    external_id = Field(attribute='external_id', column_name='id')
    flight_id = Field(attribute='flight_id', column_name='flight_id')
    time = Field(attribute='time', column_name='time', widget=DateTimeUtilWidget())
    time_received = Field(attribute='time_received', column_name='time_received', widget=DateTimeUtilWidget())
    battery_v = Field(attribute='battery_v', column_name='battery')
    cell_id = Field(attribute='cell_id', column_name='cellid')
    rsrp_dbm = Field(attribute='rsrp_dbm', column_name='rsrp')
    rsrq_db = Field(attribute='rsrq_db', column_name='rsrq')
    snr_db = Field(attribute='snr_db', column_name='snr')
    tac = Field(attribute='tac', column_name='tac')
    visible_satellites_num = Field(attribute='visible_satellites_num', column_name='satellites')
    is_charging = Field(attribute='is_charging', column_name='charging')

    class Meta:
        model = StatusDatapoint
        exclude = ['dataset']

    def __init__(self, user=None, dataset=None):
        super().__init__()

        self.status_dataset = dataset

        if dataset is not None:
            self.user = dataset.created_by
        else:
            self.user = user

    def before_import(self, dataset, using_transactions, dry_run, **kwargs):
        # for dry run it is necessary to create dataset for the validation to pass
        if dry_run and self.status_dataset is None:
            self.status_dataset = create_dry_import_dataset(self.user)

    def before_save_instance(self, instance, using_transactions, dry_run):
        instance.dataset = self.status_dataset
