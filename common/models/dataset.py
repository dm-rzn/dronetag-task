from .base_dataset import BaseDataset

# models
from django.db import models

# i18n
from django.utils.translation import gettext_lazy as _


def resolve_data_path(instance, filename):
    return f'{instance._meta.model_name}s/{filename}'


class Dataset(BaseDataset, models.Model):
    data = models.FileField(
        upload_to=resolve_data_path,
        verbose_name=_('Raw data'),
    )

    class Meta:
        abstract = True
