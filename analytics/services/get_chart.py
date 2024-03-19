# typing
from analytics.models import FlightAnalyticsDataset

# enums
from analytics.charts import ChartEnum

# charts
from analytics.charts.base import BaseChart
from analytics.charts import (
    TelemetryLatencyChart,
    StatusLatencyChart,
    RSRPChart,
    RSRQChart,
    SNRChart,
)


def get_chart(dataset: FlightAnalyticsDataset, type: ChartEnum) -> BaseChart:
    match type:
        case ChartEnum.TELEMETRY_LATENCY:
            return TelemetryLatencyChart(dataset)
        case ChartEnum.STATUS_LATENCY:
            return StatusLatencyChart(dataset)
        case ChartEnum.RSRP:
            return RSRPChart(dataset)
        case ChartEnum.RSRP_BY_TAC:
            return RSRPChart(dataset, group_by='tac')
        case ChartEnum.RSRP_BY_CELL_ID:
            return RSRPChart(dataset, group_by='cell_id')
        case ChartEnum.RSRQ:
            return RSRQChart(dataset)
        case ChartEnum.RSRQ_BY_TAC:
            return RSRQChart(dataset, group_by='tac')
        case ChartEnum.RSRQ_BY_CELL_ID:
            return RSRQChart(dataset, group_by='cell_id')
        case ChartEnum.SNR:
            return SNRChart(dataset)
        case ChartEnum.SNR_BY_TAC:
            return SNRChart(dataset, group_by='tac')
        case ChartEnum.SNR_BY_CELL_ID:
            return SNRChart(dataset, group_by='cell_id')
        # no need for default case since it should not be possible to happen since the type is passed
        # from a form using choice field
