# views
from django.views import View

# decorators
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# aux
from .get import _get
from .post import _post


class DatasetsView(View):

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return _get(request)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        return _post(request)
