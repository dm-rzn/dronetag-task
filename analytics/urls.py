# urls
from django.urls import path

# views
from .views import (
    dataset_list,
)


app_name = 'analytics'
urlpatterns = [
    path('', dataset_list, name='list'),
]
