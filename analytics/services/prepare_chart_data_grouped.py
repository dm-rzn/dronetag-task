# typing
from typing import Any


def prepare_chart_data_grouped(values: list[tuple[Any, Any, Any]]) -> tuple[list[Any], dict[str, list[Any]]]:
    labels = []
    groups = dict()

    for x, y, group in values:
        labels.append(x.isoformat())
        group_datapoints = groups.get(group, [])

        if group in groups:
            group_datapoints = groups[group]
        else:
            group_datapoints = [None] * len(labels)
            groups[group] = group_datapoints

        group_datapoints.append(y)
        for g, datapoints in groups.items():
            if g != group:
                datapoints.append(None)

    return labels, groups
