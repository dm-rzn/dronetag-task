# typing
from django.db.models import (
    QuerySet,
)

# models
from analytics.models import (
    FlightAnalytics,
)

# services
from analytics.services import (
    order_datasets,
    search_datasets,
    paginate_datasets,
)


def dataset_list_usecase(page: int, q: str) -> tuple[
    QuerySet[FlightAnalytics],
    int,
    list[int],
]:
    queryset = FlightAnalytics.objects.select_related('created_by')

    queryset = search_datasets(queryset, term=q)
    queryset = order_datasets(queryset, order_by_fields=('-created_at', ))  # TODO: make this changeable
    queryset, page, page_range = paginate_datasets(queryset, page_number=page)  # TODO: per_page changeable

    return queryset, page, page_range
