from abc import ABC, abstractmethod

# typing
from tablib import Dataset


class AbstractLoader(ABC):
    @abstractmethod
    def load(self, dataset: Dataset):
        ...
