from .latency import LatencyChart

# i18n
from django.utils.translation import gettext as _


class StatusLatency(LatencyChart):
    _title = _('Status Latency')

    def _data(self):
        return list(
            self.dataset.statuses.datapoints
            .order_by('time')
            .values_list('time', 'latency')
        )
