# typing
from django.db.models import (
    QuerySet,
)

# models
from analytics.models import (
    FlightAnalytics,
)


def order_datasets(
    queryset: QuerySet[FlightAnalytics],
    order_by_fields: tuple[str] = ('-created_at', )
) -> QuerySet[FlightAnalytics]:
    return queryset.order_by(*order_by_fields)
