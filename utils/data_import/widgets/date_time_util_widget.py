# django-import-export
from import_export.widgets import Widget

# dateutil
from dateutil.parser import parse


class DateTimeUtilWidget(Widget):
    """
    Uses dateutil instead of datetime.
    """

    def clean(self, value, row=None, **kwargs):
        try:
            return parse(value)
        except Exception:
            raise ValueError("Enter a valid date/time.")

    def render(self, value, obj=None):
        if not value:
            return ''
        return value.isoformat()
