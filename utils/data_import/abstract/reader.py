from abc import ABC, abstractmethod

# typing
from tablib import Dataset
from django.core.files.base import File


class AbstractReader(ABC):
    @abstractmethod
    def read(self, file: File) -> Dataset:
        ...
