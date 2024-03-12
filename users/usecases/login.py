# http
from django.http import HttpRequest

# auth
from django.contrib.auth import (
    authenticate,
    login,
)


def login_usecase(request: HttpRequest, username: str, password: str) -> bool:
    user = authenticate(request, username=username, password=password)

    logged_in = user is not None
    if logged_in:
        login(request, user)

    return logged_in
