# models
from django.db import models

# urls
from django.urls import reverse

from common.models import BaseDataset
from statuses.models import StatusDataset
from telemetry.models import TelemetryDataset

# i18n
from django.utils.translation import gettext_lazy as _


class FlightAnalyticsDataset(BaseDataset, models.Model):
    telemetry = models.ForeignKey(
        TelemetryDataset,
        on_delete=models.PROTECT,
        related_name='flight_analytics',
        verbose_name=_('Telemetry dataset'),
    )
    statuses = models.ForeignKey(
        StatusDataset,
        on_delete=models.PROTECT,
        related_name='flight_analytics',
        verbose_name=_('Status dataset'),
    )

    class Meta:
        verbose_name = verbose_name_plural = _('Flight analytics')

    def get_absolute_url(self):
        return reverse('analytics:dataset-detail', kwargs={'id': self.id})
