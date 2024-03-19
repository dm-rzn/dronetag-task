# views
from django.views import View

# decorators
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# aux
from .get import _get


class DatasetDetailView(View):

    @method_decorator(login_required)
    def get(self, request, id: int, *args, **kwargs):
        return _get(request, id)
