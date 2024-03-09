# models
from django.db import models

# conf
from django.conf import settings

# i18n
from django.utils.translation import gettext_lazy as _

# constants
from .constants import (
    COORDINATE_PRECISION,
    LATITUDE_DIGITS,
    LONGITUDE_DIGITS,
    ALTITUDE_PRECISION,
    ALTITUDE_DIGITS,
    HEIGHT_PRECISION,
    HEIGHT_DIGITS,
    VELOCITY_PRECISION,
    VELOCITY_DIGITS,
    PRESSURE_PRECISION,
    PRESSURE_DIGITS,
    TELEMETRY_PATH,
)


class TelemetryDataset(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name=_('Name'),
    )
    data = models.FileField(
        upload_to=TELEMETRY_PATH,
        verbose_name=_('Raw data'),
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='created_telemetry_datasets',
        on_delete=models.PROTECT,  # either way, django discourages user deletion
        verbose_name=_('Created by'),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Created at'),
    )

    class Meta:
        verbose_name = _('Telemetry dataset')
        verbose_name_plural = _('Telemetry datasets')

    def __str__(self):
        return self.name


class TelemetryDatapoint(models.Model):
    dataset = models.ForeignKey(
        TelemetryDataset,
        on_delete=models.CASCADE,
        related_name='datapoints',
        verbose_name=_('Dataset'),
    )
    external_id = models.PositiveBigIntegerField(
        verbose_name=_('External ID'),
    )
    time = models.DateTimeField(
        verbose_name=_('Time'),
        help_text=_('Datapoint time'),
    )
    time_received = models.DateTimeField(
        verbose_name=_('Time received'),
        help_text=_('Time when this message was received on server.'),
    )
    latitude = models.DecimalField(
        max_digits=LATITUDE_DIGITS,
        decimal_places=COORDINATE_PRECISION,
        verbose_name=_('Latitude'),
    )
    longitude = models.DecimalField(
        max_digits=LONGITUDE_DIGITS,
        decimal_places=COORDINATE_PRECISION,
        verbose_name=_('Longitude'),
    )
    altitude_m = models.DecimalField(
        max_digits=ALTITUDE_DIGITS,
        decimal_places=ALTITUDE_PRECISION,
        verbose_name=_('Altitude [m]'),
        help_text=_('Altitude calculated from pressure sensor (QNH referece) in meters'),
    )
    geo_altitude_m = models.DecimalField(
        max_digits=ALTITUDE_DIGITS,
        decimal_places=ALTITUDE_PRECISION,
        verbose_name=_('Geo altitude [m]'),
        help_text=_('Altitude supplied from the GNSS received (geoid reference) in meters.'),
    )
    height_m = models.DecimalField(
        max_digits=HEIGHT_DIGITS,
        decimal_places=HEIGHT_PRECISION,
        verbose_name=_('Height [m]'),
        help_text=_('Relative altitude from the takeoffpoint in meters.'),
    )
    velocity_x_ms = models.DecimalField(
        max_digits=VELOCITY_DIGITS,
        decimal_places=VELOCITY_PRECISION,
        verbose_name=_('X velocity [m/s]'),
    )
    velocity_y_ms = models.DecimalField(
        max_digits=VELOCITY_DIGITS,
        decimal_places=VELOCITY_PRECISION,
        verbose_name=_('Y velocity [m/s]'),
    )
    velocity_z_ms = models.DecimalField(
        max_digits=VELOCITY_DIGITS,
        decimal_places=VELOCITY_PRECISION,
        verbose_name=_('Z velocity [m/s]'),
    )
    vertical_accuracy_m = models.PositiveSmallIntegerField(
        verbose_name=_('Vertical accuracy [m]'),
    )
    horizontal_accuracy_m = models.PositiveSmallIntegerField(
        verbose_name=_('Horizontal accuracy [m]'),
    )
    velocity_accuracy_ms = models.PositiveSmallIntegerField(
        verbose_name=_('Velocity accuracy [m/s]'),
    )
    pressure_hpa = models.DecimalField(
        max_digits=PRESSURE_DIGITS,
        decimal_places=PRESSURE_PRECISION,
        verbose_name=_('Pressure [hPa]'),
    )

    class Meta:
        verbose_name = _('Telemetry datapoint')
        verbose_name_plural = _('Telemetry datapoints')
        unique_together = [
            ('dataset', 'external_id'),
        ]

    def __str__(self):
        return f'Datapoint {self.external_id}'
