# models
from analytics.models import FlightAnalyticsDataset

# enums
from analytics.charts import ChartEnum
from analytics.charts.base import BaseChart

# exceptions
from analytics.exceptions import FlightAnalyticsDatasetDoesNotExist

# services
from analytics.services import get_chart


def dataset_detail_usecase(id: int, chart_type: ChartEnum) -> tuple[
    FlightAnalyticsDataset,
    BaseChart,
    list[tuple[int, str]],
]:
    '''
    :raises: FlightAnalyticsDatasetDoesNotExist
    '''
    try:
        dataset = FlightAnalyticsDataset.objects.get(id=id)
    except FlightAnalyticsDataset.DoesNotExist:
        raise FlightAnalyticsDatasetDoesNotExist()  # reraise as custom exception

    chart = get_chart(dataset, chart_type)

    return dataset, chart, ChartEnum.choices
