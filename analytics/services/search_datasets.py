# typing
from django.db.models import (
    QuerySet,
)

# models
from analytics.models import (
    FlightAnalyticsDataset,
)


def search_datasets(queryset: QuerySet[FlightAnalyticsDataset], term: str) -> QuerySet[FlightAnalyticsDataset]:
    # TODO: inneficient and simplistic
    if term is not None and term.strip():
        return queryset.filter(name__icontains=term)
    else:
        return queryset
