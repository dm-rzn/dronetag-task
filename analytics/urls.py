# urls
from django.urls import path

# views
from .views import (
    DatasetsView,
    new_dataset,
)


app_name = 'analytics'
urlpatterns = [
    path('', DatasetsView.as_view(), name='datasets'),
    path('new', new_dataset, name='new'),
]
