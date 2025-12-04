from pymongo import MongoClient
from sinks.base_sink import BaseSink

class MongoDBSink(BaseSink):
    def __init__(self, config):
        super().__init__(config)
        self.host = config['host']
        self.port = config['port']
        self.database = config['database']
        self.collection = config['collection']

        self.client = None
        self.db = None
        self.collection_obj = None

    def connect(self):
        try:
            self.client = MongoClient(host=self.host, port=self.port)
            self.db = self.client[self.database]
            self.collection_obj = self.db[self.collection]
            print("Connected to MongoDB")
        except Exception as e:
            print(f"Error connecting to MongoDB: {e}")

    def write(self, data):
        """
        Writes data to a MongoDB collection.
        """
        if not self.client or not self.db or not self.collection_obj:
            self.connect()

        try:
            self.collection_obj.insert_one(data)
        except Exception as e:
            print(f"Error writing to MongoDB: {e}")

    def close(self):
        if self.client:
            self.client.close()
            print("Closed MongoDB connection")