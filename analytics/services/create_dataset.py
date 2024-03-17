# models
from analytics.models import FlightAnalyticsDataset

# typing
from telemetry.models import TelemetryDataset
from statuses.models import StatusDataset
from users.models import User


def create_dataset(
    name: str,
    telemetry: TelemetryDataset,
    status: StatusDataset,
    created_by: User
) -> FlightAnalyticsDataset:
    return FlightAnalyticsDataset.objects.create(
        name=name,
        telemetry=telemetry,
        statuses=status,
        created_by=created_by,
    )
