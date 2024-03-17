# shortcuts
from django.shortcuts import (
    render,
    redirect,
)

# forms
from analytics.forms import DatasetCreateForm

# exceptions
from telemetry.exceptions import TelemetryException
from statuses.exceptions import StatusException

# usecases
from analytics.usecases import dataset_create_usecase

# i18n
from django.utils.translation import gettext_lazy as _


def _post(request):
    form = DatasetCreateForm(
        {
            **request.POST,
            'created_by': request.user,
        },
        files=request.FILES,
    )

    if not form.is_valid():
        ...  # TODO

    telemetry = request.FILES['telemetry']
    status = request.FILES['status']

    try:
        obj = dataset_create_usecase(
            name=form.cleaned_data['name'],
            telemetry_data=telemetry,
            status_data=status,
            user=request.user,
        )
    except TelemetryException:
        return render(
            request,
            'analytics/new/full.html',
            context={
                # TODO
                'telemetry_error': _('Telemetry dataset cannot be imported.')
            }
        )
    except StatusException:
        return render(
            request,
            'analytics/new/full.html',
            context={
                # TODO
                'status_error': _('Status dataset cannot be imported.')
            }
        )

    return redirect(to=obj)
