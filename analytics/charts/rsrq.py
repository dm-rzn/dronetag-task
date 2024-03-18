# base
from .line import LineChart

# i18n
from django.utils.translation import gettext as _

# typing
from django.db.models import QuerySet


class RSRQChart(LineChart):
    template = 'charts/rsrq.html'
    title = _('RSRQ')
    y_label = _('RSRQ [db]')
    fields = ('time', 'rsrq_db')

    def queryset(self) -> QuerySet:
        return self.dataset.statuses.datapoints
