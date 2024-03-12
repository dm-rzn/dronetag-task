from abc import ABC, abstractmethod

# typing
from tablib import Dataset


class AbstractReader(ABC):
    @abstractmethod
    def read(self) -> Dataset:
        ...
