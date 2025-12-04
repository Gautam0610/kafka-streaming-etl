from abc import ABC, abstractmethod

class BaseProcessor(ABC):
    def __init__(self, config):
        self.config = config

    @abstractmethod
    def process(self, data):
        """
        Abstract method to process the data.
        """
        pass