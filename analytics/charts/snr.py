# base
from .line import LineChart

# i18n
from django.utils.translation import gettext as _

# typing
from django.db.models import QuerySet


class SNRChart(LineChart):
    template = 'charts/snr.html'
    title = _('SNR')
    y_label = _('SNR [db]')
    fields = ('time', 'snr_db')

    def queryset(self) -> QuerySet:
        return self.dataset.statuses.datapoints
