from abc import ABC, abstractmethod

class BaseConnector(ABC):
    def __init__(self, config):
        self.config = config

    @abstractmethod
    def read(self):
        """
        Abstract method to read data from the source.
        """
        pass