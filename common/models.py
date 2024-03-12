# models
from django.db import models

# conf
from django.conf import settings

# i18n
from django.utils.translation import gettext_lazy as _


def resolve_data_path(instance, filename):
    return f'{instance._meta.model_name}s/{filename}'


class Base(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name=_('Name'),
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='created_%(class)ss',
        on_delete=models.PROTECT,  # either way, django discourages user deletion
        verbose_name=_('Created by'),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Created at'),
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Dataset(Base, models.Model):
    data = models.FileField(
        upload_to=resolve_data_path,
        verbose_name=_('Raw data'),
    )

    class Meta:
        abstract = True
