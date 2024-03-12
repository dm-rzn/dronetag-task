# typing
from django.db.models import (
    QuerySet,
)

# models
from analytics.models import (
    FlightAnalytics,
)


def search_datasets(queryset: QuerySet[FlightAnalytics], term: str) -> QuerySet[FlightAnalytics]:
    # TODO: inneficient and simplistic
    return queryset.filter(name__icontains=term)
