# shortcuts
from django.shortcuts import (
    render,
)

# decorators
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET

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


@require_GET
@login_required
def dataset_list(request):
    form = DatasetListForm(request.GET)
    if not form.is_valid():
        ...

    datasets, page, page_range = dataset_list_usecase(
        page=form.cleaned_data['page'] or 1,
        q=form.cleaned_data['q'] or '',
    )

    return render(
        request,
        get_template(request, 'dataset_list'),
        context={
            'datasets': datasets,
            'page': page,
            'page_range': page_range,
        }
    )
