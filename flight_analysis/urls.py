from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from django.http import HttpResponse


urlpatterns = [
    path('admin/', admin.site.urls),
    path('-/health-checks/readiness', lambda request: HttpResponse()),
    path('-/health-checks/liveness', lambda request: HttpResponse()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
