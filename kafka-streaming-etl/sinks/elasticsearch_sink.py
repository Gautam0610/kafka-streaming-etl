from elasticsearch import Elasticsearch
from sinks.base_sink import BaseSink

class ElasticsearchSink(BaseSink):
    def __init__(self, config):
        super().__init__(config)
        self.host = config['host']
        self.port = config['port']
        self.index = config['index']

        self.es = None

    def connect(self):
        try:
            self.es = Elasticsearch([{'host': self.host, 'port': self.port}])
            if self.es.ping():
                print("Connected to Elasticsearch")
            else:
                print("Failed to connect to Elasticsearch")
                self.es = None
        except Exception as e:
            print(f"Error connecting to Elasticsearch: {e}")

    def write(self, data):
        """
        Writes data to an Elasticsearch index.
        """
        if not self.es:
            self.connect()

        try:
            self.es.index(index=self.index, document=data)
        except Exception as e:
            print(f"Error writing to Elasticsearch: {e}")

    def close(self):
        if self.es:
            # Elasticsearch client doesn't have a close method, so nothing to do here
            print("Elasticsearch connection closed (if applicable)")