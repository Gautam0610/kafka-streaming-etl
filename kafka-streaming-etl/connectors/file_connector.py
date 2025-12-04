import os
from connectors.base_connector import BaseConnector

class FileConnector(BaseConnector):
    def __init__(self, config):
        super().__init__(config)
        self.path = config['path']

    def read(self):
        """
        Reads data from a file.
        """
        try:
            with open(self.path, 'r') as f:
                return f.readlines()
        except FileNotFoundError:
            print(f"Error: File not found at path: {self.path}")
            return None
        except Exception as e:
            print(f"Error reading file: {e}")
            return None