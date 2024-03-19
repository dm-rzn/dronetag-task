# base
from .line import LineChart

from django.db.models.functions import Extract

# i18n
from django.utils.translation import gettext as _


class LatencyChart(LineChart):
    template = 'charts/latency.html'
    title = _('Latency')
    y_label = _('Latency [ms]')
    fields = ('time', Extract('latency', 'milliseconds'))
