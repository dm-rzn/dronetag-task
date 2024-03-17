# typing
from django.db.models import (
    QuerySet,
)

# pagination
from django.core.paginator import (
    Paginator,
)

# models
from analytics.models import (
    FlightAnalyticsDataset,
)


DEFAULT_PER_PAGE = 20
MAX_PER_PAGE = 60


def paginate_datasets(
    queryset: QuerySet[FlightAnalyticsDataset],
    page_number: int = 1,
    per_page: int = DEFAULT_PER_PAGE
) -> tuple[
    QuerySet[FlightAnalyticsDataset],
    int,
    list[int],
]:
    if per_page <= 0:
        per_page = DEFAULT_PER_PAGE
    per_page = min(per_page, MAX_PER_PAGE)

    if page_number is None or page_number < 1:
        page_number = 1

    paginator = Paginator(queryset, per_page)
    page = paginator.get_page(page_number)

    return page.object_list, page, paginator.get_elided_page_range(page_number)
