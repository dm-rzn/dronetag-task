# typing
from django.db.models import (
    QuerySet,
)

# models
from analytics.models import (
    FlightAnalyticsDataset,
)


def order_datasets(
    queryset: QuerySet[FlightAnalyticsDataset],
    order_by_fields: tuple[str] = ('-created_at', )
) -> QuerySet[FlightAnalyticsDataset]:
    return queryset.order_by(*order_by_fields)
