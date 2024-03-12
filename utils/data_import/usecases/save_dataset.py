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
from django import forms
from common.models import Dataset


def save_dataset(form: forms.ModelForm, resource: resources.Resource) -> Dataset:
    dataset = form.save()
    reader = create_reader(dataset.data)
    loader = create_loader(reader=reader, dataset=dataset, resource=resource)
    try:
        loader.load()
    except (ReaderException, LoaderException):
        # TODO: log
        ...  # TODO: handle

    return dataset
