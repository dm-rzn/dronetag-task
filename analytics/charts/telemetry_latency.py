from .latency import LatencyChart

# i18n
from django.utils.translation import gettext as _

# typing
from django.db.models import QuerySet


class TelemetryLatencyChart(LatencyChart):
    title = _('Telemetry Latency')

    def queryset(self) -> QuerySet:
        return self.dataset.telemetry.datapoints
