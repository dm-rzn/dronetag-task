# models
from django.db import models

# i18n
from django.utils.translation import gettext as _


class ChartEnum(models.IntegerChoices):
    TELEMETRY_LATENCY = 1, _('Telemetry latency')
    STATUS_LATENCY = 2, _('Status latency')
    RSRP = 3, _('RSRP')
    RSRP_BY_TAC = 4, _('RSRP by TAC')
    RSRP_BY_CELL_ID = 5, _('RSRP by Cell ID')
    RSRQ = 6, _('RSRQ')
    RSRQ_BY_TAC = 7, _('RSRQ by TAC')
    RSRQ_BY_CELL_ID = 8, _('RSRQ by Cell ID')
    SNR = 9, _('SNR')
    SNR_BY_TAC = 10, _('SNR by TAC')
    SNR_BY_CELL_ID = 11, _('SNR by Cell ID')
