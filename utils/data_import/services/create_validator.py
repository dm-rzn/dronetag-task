from utils.data_import.validators import Validator

# resources
from import_export import resources

# typing
from common.models import Dataset
from users.models import User
from utils.data_import.abstract.reader import AbstractReader
from utils.data_import.abstract.validator import AbstractValidator


def create_validator(
    reader: AbstractReader,
    user: User,
    resource: resources.Resource,
    dataset: Dataset = None,
) -> AbstractValidator:
    return Validator(reader=reader, user=user, dataset=dataset, resource=resource)
