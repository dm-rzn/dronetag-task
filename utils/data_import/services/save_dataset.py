# services
from utils.data_import.services import (
    create_reader,
    create_loader,
)

# resources
from import_export import resources

# exceptions
from utils.data_import.exceptions import (
    ReaderException,
    LoaderException,
)

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
    try:
        loader.load()
    except (ReaderException, LoaderException) as e:
        logger.error(f'save_dataset - { dataset = } - { resource = } - load failed - {e}')
        raise

    return dataset
