from django.http import HttpRequest


def get_template(request: HttpRequest, path: str) -> str:
    name = 'partial' if request.htmx else 'full'

    return f'{path}/{name}.html'
