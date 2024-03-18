# utils
from django.template.loader import get_template

# typing
from analytics.models import FlightAnalyticsDataset
from typing import Any


class BaseChart:
    template: str = ''
    title: str = ''

    def __init__(self, dataset: FlightAnalyticsDataset):
        self.dataset = dataset

    def _context(self) -> dict[str, Any]:
        return {}

    def render(self, request):
        return get_template(self.template).render(context=self._context(), request=request).strip()
