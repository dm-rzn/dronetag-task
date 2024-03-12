from utils.data_import.loaders import Loader

# resources
from import_export import resources

# typing
from common.models import Dataset
from utils.data_import.abstract.reader import AbstractReader
from utils.data_import.abstract.loader import AbstractLoader


def create_loader(reader: AbstractReader, dataset: Dataset, resource: resources.Resource) -> AbstractLoader:
    return Loader(reader=reader, dataset=dataset, resource=resource)
