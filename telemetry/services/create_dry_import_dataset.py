# models
from telemetry.models import TelemetryDataset


def create_dry_import_dataset(user) -> TelemetryDataset:
    return TelemetryDataset.objects.create(name='dry_run', created_by=user)
