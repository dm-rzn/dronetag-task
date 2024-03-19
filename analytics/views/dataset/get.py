# shortcuts
from django.shortcuts import (
    render,
)
from django.http import Http404

# usecases
from analytics.usecases import dataset_detail_usecase

# services
from common.services import get_template

# exceptions
from analytics.exceptions import FlightAnalyticsDatasetDoesNotExist

# forms
from analytics.forms import DatasetDetailForm


def _get(request, id: int):
    form = DatasetDetailForm(request.GET)
    if not form.is_valid():
        ...  # TODO

    try:
        dataset, chart, chart_choices = dataset_detail_usecase(id, form.cleaned_data['chart'])
    except FlightAnalyticsDatasetDoesNotExist:
        raise Http404("No dataset for the given ID.")

    return render(
        request,
        get_template(request, 'analytics/dataset_detail'),
        context={
            'chart': chart.render(request),
            'chart_choices': chart_choices,
            'selected_chart': form.cleaned_data['chart'],
            'dataset': dataset,
        }
    )
