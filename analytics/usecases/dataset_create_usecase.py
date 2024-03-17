# transactions
from django.db import transaction

# models
from analytics.models import (
    FlightAnalyticsDataset,
)

# services
from telemetry.services import (
    validate_telemetry_dataset,
    save_telemetry_dataset,
)
from statuses.services import (
    validate_status_dataset,
    save_status_dataset,
)
from analytics.services import (
    create_dataset,
)

# typing
from django.core.files.base import File
from users.models import User


@transaction.atomic
def dataset_create_usecase(name: str, telemetry_data: File, status_data: File, user: User) -> FlightAnalyticsDataset:
    validate_telemetry_dataset(telemetry_data, user)
    validate_status_dataset(status_data, user)

    telemetry_dataset = save_telemetry_dataset(f'[telemetry] {name}', telemetry_data, user)
    status_dataset = save_status_dataset(f'[status] {name}', status_data, user)

    return create_dataset(name, telemetry_dataset, status_dataset, user)
