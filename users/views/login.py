# shortcuts
from django.shortcuts import (
    redirect,
    render,
)

# forms
from users.forms import (
    LoginForm,
)

# usecases
from users.usecases import (
    login_usecase,
)


def _get_login_view(request):
    form = LoginForm()

    return render(request, 'login.html', {'form': form})


def _post_login_view(request):
    form = LoginForm(request.POST)
    if (
        form.is_valid()
        and login_usecase(
            request,
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
        )
    ):
        return redirect('analytics:list')

    return render(request, 'login.html', {'form': form})


def login_view(request):
    if request.POST:
        return _post_login_view(request)
    else:
        return _get_login_view(request)
