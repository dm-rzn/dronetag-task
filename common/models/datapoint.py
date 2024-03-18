# models
from django.db import models
from django.db.models import F

# i18n
from django.utils.translation import gettext_lazy as _


class Datapoint(models.Model):
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

    class Meta:
        abstract = True
