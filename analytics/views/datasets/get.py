# shortcuts
from django.shortcuts import (
    render,
)

# forms
from analytics.forms import (
    DatasetListForm,
)

# usecases
from analytics.usecases import (
    dataset_list_usecase,
)

# services
from common.services import get_template


def _get(request):
    form = DatasetListForm(request.GET)
    if not form.is_valid():
        ...  # TODO

    datasets, page, page_range = dataset_list_usecase(
        page=form.cleaned_data['page'] or 1,
        q=form.cleaned_data['q'] or '',
    )

    return render(
        request,
        get_template(request, 'analytics/dataset_list'),
        context={
            'datasets': datasets,
            'page': page,
            'page_range': page_range,
        }
    )
