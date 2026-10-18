
from abc import ABC, abstractmethod


class HealCapability(ABC):
    @abstractmethod
    def heal(self):
        pass


class TransformCapability(ABC):
    def __init__(self):
        self.is_transformed = False

    @abstractmethod
    def transform(self):
        pass

    @abstractmethod
    def revert(self):
        pass
