import boto3
import json
from sinks.base_sink import BaseSink

class S3Sink(BaseSink):
    def __init__(self, config):
        super().__init__(config)
        self.bucket_name = config['bucket_name']
        self.prefix = config['prefix']
        self.aws_access_key_id = config['aws_access_key_id']
        self.aws_secret_access_key = config['aws_secret_access_key']
        self.s3 = None

    def connect(self):
        try:
            self.s3 = boto3.client(
                's3',
                aws_access_key_id=self.aws_access_key_id,
                aws_secret_access_key=self.aws_secret_access_key
            )
            print("Connected to S3")
        except Exception as e:
            print(f"Error connecting to S3: {e}")

    def write(self, data):
        """
        Writes data to an S3 bucket.
        """
        if not self.s3:
            self.connect()

        try:
            key = f"{self.prefix}/{data['id']}.json"  # Assuming data has an 'id' field
            self.s3.put_object(
                Bucket=self.bucket_name,
                Key=key,
                Body=json.dumps(data)
            )
        except Exception as e:
            print(f"Error writing to S3: {e}")
    
    def close(self):
        # boto3 client doesn't have a close method, so nothing to do here
        print("S3 connection closed (if applicable)")