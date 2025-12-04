from abc import ABC, abstractmethod

class BaseValidator(ABC):
    def __init__(self, config):
        self.config = config

    @abstractmethod
    def validate(self, data):
        """Abstract method to validate data"""
        pass