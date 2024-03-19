# typing
from typing import Any


def prepare_chart_data(values: list[tuple[Any, Any]], label: str) -> tuple[list[Any], dict[str, list[Any]]]:
    labels = []
    datapoints = []
    for x, y in values:
        labels.append(x.isoformat())
        datapoints.append(y)

    return labels, {label: datapoints}
