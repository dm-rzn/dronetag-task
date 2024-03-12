# models
from statuses.models import StatusDataset

# typing
from users.models import User


def create_dry_import_dataset(user: User) -> StatusDataset:
    return StatusDataset.objects.create(name='dry_run', created_by=user)