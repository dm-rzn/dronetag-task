# services
from utils.data_import.services import (
    create_reader,
    create_loader,
)

# resources
from import_export import resources

# typing
from common.models import Dataset

# loging
import logging

logger = logging.getLogger('django')


def save_dataset(dataset: Dataset, resource: resources.Resource) -> Dataset:
    '''
    :raises: ReaderException
    :raises: LoaderException
    '''
    reader = create_reader(dataset.data)
    loader = create_loader(reader=reader, dataset=dataset, resource=resource)

    loader.load()

    return dataset
