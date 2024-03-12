# models
from django.db import models
from common.models import Dataset

# typing
from users.models import User


def create_dry_import_dataset(user: User, dataset_model: models.Model) -> Dataset:
    return dataset_model.objects.create(name='dry_run', created_by=user)
