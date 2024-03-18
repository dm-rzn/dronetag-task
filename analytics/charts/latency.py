# base
from .base import BaseChart

# i18n
from django.utils.translation import gettext as _

# typing
from typing import Any
from datetime import (
    datetime,
    timedelta,
)


class LatencyChart(BaseChart):
    _template = 'charts/latency.html'
    _title = _('Latency')

    def _data(self) -> list[tuple[datetime, timedelta]]:
        return []

    def _context(self) -> dict[str, Any]:
        values = self._data()
        labels = []
        datapoints = []
        for time, latency in values:
            labels.append(time.isoformat())
            datapoints.append(latency.microseconds / 1_000)

        return {
            'title': self._title,
            'labels': labels,
            'datapoints': datapoints,
        }
