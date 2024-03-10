from abc import ABC, abstractmethod

# typing
from tablib import Dataset


class AbstractValidator(ABC):
    @abstractmethod
    def validate(self, dataset: Dataset):
        ...
