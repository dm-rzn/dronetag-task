from .latency import LatencyChart

# i18n
from django.utils.translation import gettext as _

# typing
from django.db.models import QuerySet


class StatusLatencyChart(LatencyChart):
    title = _('Status Latency')

    def queryset(self) -> QuerySet:
        return self.dataset.statuses.datapoints
