# shortcuts
from django.shortcuts import (
    render,
)

# decorators
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET


@require_GET
@login_required
def new_dataset(request):
    return render(
        request,
        'analytics/new/full.html',
        context={},
    )
