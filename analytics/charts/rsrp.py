# base
from .line import LineChart

# i18n
from django.utils.translation import gettext as _

# typing
from django.db.models import QuerySet


class RSRPChart(LineChart):
    template = 'charts/rsrp.html'
    title = _('RSRP')
    y_label = _('RSRP [dbm]')
    fields = ('time', 'rsrp_dbm')

    def queryset(self) -> QuerySet:
        return self.dataset.statuses.datapoints
