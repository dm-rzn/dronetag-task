# models
from telemetry.models import TelemetryDataset

# typing
from users.models import User


def create_dry_import_dataset(user: User) -> TelemetryDataset:
    return TelemetryDataset.objects.create(name='dry_run', created_by=user)
