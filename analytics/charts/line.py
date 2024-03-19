# base
from .base import BaseChart

# services
from analytics.services import (
    prepare_chart_data,
    prepare_chart_data_grouped,
)

# typing
from typing import Any
from analytics.models import FlightAnalyticsDataset
from datetime import datetime
from django.db.models import QuerySet


class LineChart(BaseChart):
    y_label: str = ''

    def __init__(self, dataset: FlightAnalyticsDataset, group_by: str = None):
        super().__init__(dataset)
        self.group_by = group_by

    def queryset(self) -> QuerySet:
        raise NotImplementedError()

    def _data(self) -> list[tuple[datetime, Any]] | list[tuple[datetime, Any, Any]]:
        fields = (*self.fields, self.group_by, ) if self.group_by else self.fields

        return (
            self.queryset()
            .order_by('time')
            .values_list(*fields)
        )

    def _prepare_chart_data(self) -> tuple[list[Any], dict[str, list[Any]]]:
        if self.group_by:
            return prepare_chart_data_grouped(self._data())
        else:
            return prepare_chart_data(self._data(), label=self.title)

    def _context(self) -> dict[str, Any]:
        labels, datasets = self._prepare_chart_data()

        return {
            'title': self.title,
            'y_label': self.y_label,
            'labels': labels,
            'sets': datasets,
        }
