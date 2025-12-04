from abc import ABC, abstractmethod

class BaseSink(ABC):
    def __init__(self, config):
        self.config = config

    @abstractmethod
    def write(self, data):
        """
        Abstract method to write data to the destination.
        """
        pass