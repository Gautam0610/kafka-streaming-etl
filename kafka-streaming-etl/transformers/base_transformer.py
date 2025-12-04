from abc import ABC, abstractmethod

class BaseTransformer(ABC):
    def __init__(self, config):
        self.config = config

    @abstractmethod
    def transform(self, data):
        """Abstract method to transform data"""
        pass