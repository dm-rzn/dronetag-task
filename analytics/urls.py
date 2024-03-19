# urls
from django.urls import path

# views
from .views import (
    DatasetsView,
    DatasetDetailView,
    new_dataset,
)


app_name = 'analytics'
urlpatterns = [
    path('', DatasetsView.as_view(), name='datasets'),
    path('<int:id>/', DatasetDetailView.as_view(), name='dataset-detail'),
    path('new/', new_dataset, name='new'),
]
