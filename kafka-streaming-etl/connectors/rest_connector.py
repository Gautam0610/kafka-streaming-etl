import requests
from connectors.base_connector import BaseConnector

class RESTConnector(BaseConnector):
    def __init__(self, config):
        super().__init__(config)
        self.url = config['url']

    def read(self):
        """
        Reads data from a REST API endpoint.
        """
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from REST API: {e}")
            return None