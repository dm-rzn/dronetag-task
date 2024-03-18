# models
from django.db import models
from django.db.models import F

from common.models import Dataset

# i18n
from django.utils.translation import gettext_lazy as _

# constants
from .constants import (
    FLIGHT_ID_LENGTH,
    BATTERY_DIGITS,
    BATTERY_PRECISION,
    CELL_ID_LENGTH,
    TAC_LENGTH,
)


class StatusDataset(Dataset, models.Model):

    class Meta:
        verbose_name = _('Status dataset')
        verbose_name_plural = _('Status datasets')


class StatusDatapoint(models.Model):
    dataset = models.ForeignKey(
        StatusDataset,
        on_delete=models.CASCADE,
        related_name='datapoints',
        verbose_name=_('Dataset'),
    )
    external_id = models.PositiveBigIntegerField(
        verbose_name=_('External ID'),
    )
    flight_id = models.CharField(
        max_length=FLIGHT_ID_LENGTH,
        verbose_name=_('Flight ID'),
    )
    time = models.DateTimeField(
        verbose_name=_('Time'),
        help_text=_('Datapoint time'),
    )
    time_received = models.DateTimeField(
        verbose_name=_('Time received'),
        help_text=_('Time when this message was received on server.'),
    )
    latency = models.GeneratedField(
        expression=F('time_received') - F('time'),
        output_field=models.DurationField(),
        db_persist=True,
    )
    battery_v = models.DecimalField(
        max_digits=BATTERY_DIGITS,
        decimal_places=BATTERY_PRECISION,
        verbose_name=_('Battery voltage [V]'),
    )
    cell_id = models.CharField(
        max_length=CELL_ID_LENGTH,
        verbose_name=_('Cell ID'),
        help_text=_('ID of the current LTE cell station.'),
    )
    rsrp_dbm = models.SmallIntegerField(
        verbose_name=_('RSRP [dBm]'),
        help_text=_('Reference Signal Received Power of LTE in decibelmiliwatts (dBm).'),
    )
    rsrq_db = models.SmallIntegerField(
        verbose_name=_('RSRQ [dB]'),
        help_text=_('Reference Signal Received Quality of LTE in decibels (dB).'),
    )
    snr_db = models.SmallIntegerField(
        verbose_name=_('SNR [dB]'),
        help_text=_('Signal to Noise Ratio of LTE in decibels (dB).'),
    )
    tac = models.CharField(
        max_length=TAC_LENGTH,
        verbose_name=_('TAC'),
        help_text=_('Tracking Area Code of LTE.'),
    )
    visible_satellites_num = models.PositiveSmallIntegerField(
        verbose_name=_('Number of visible GNSS satellites'),
    )
    is_charging = models.BooleanField(
        verbose_name=_('Charging?'),
    )

    class Meta:
        verbose_name = _('Status datapoint')
        verbose_name_plural = _('Status datapoints')
        unique_together = [
            ('dataset', 'external_id'),
            ('external_id', 'flight_id'),
        ]

    def __str__(self):
        return f'Datapoint {self.flight_id} | {self.external_id}'
