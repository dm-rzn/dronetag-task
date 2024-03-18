from .latency import LatencyChart

# i18n
from django.utils.translation import gettext as _


class TelemetryLatency(LatencyChart):
    _title = _('Telemetry Latency')

    def _data(self):
        return list(
            self.dataset.telemetry.datapoints
            .order_by('time')
            .values_list('time', 'latency')
        )
