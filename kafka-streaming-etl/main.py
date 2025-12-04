import logging
import json

from connectors.rest_connector import RESTConnector
from processors.transformation_processor import TransformationProcessor
from processors.validation_processor import ValidationProcessor
from sinks.postgres_sink import PostgreSQLSink
from transformers.base_transformer import BaseTransformer
from validators.base_validator import BaseValidator

class SampleTransformer(BaseTransformer):
    def transform(self, data):
        # Example transformation: convert values to uppercase
        return {k: str(v).upper() for k, v in data.items()}

class SampleValidator(BaseValidator):
    def validate(self, data):
        # Example validation: check if 'id' exists and is a positive integer
        return 'id' in data and isinstance(data['id'], int) and data['id'] > 0

def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info("Starting Kafka Streaming ETL Pipeline")

    # 1. Configure the components
    rest_config = {'url': 'https://jsonplaceholder.typicode.com/todos/1'}
    postgres_config = {
        'host': 'localhost',
        'port': 5432,
        'database': 'mydatabase',
        'user': 'myuser',
        'password': 'mypassword',
        'table': 'mytable'
    }

    # 2. Instantiate the connectors, processors, and sinks
    rest_connector = RESTConnector(rest_config)
    
    # Create transformer and validator instances
    sample_transformer = SampleTransformer({})
    sample_validator = SampleValidator({})

    transformation_processor = TransformationProcessor({}, sample_transformer)
    validation_processor = ValidationProcessor({}, sample_validator)
    postgres_sink = PostgreSQLSink(postgres_config)

    # 3. Read data from the source
    data = rest_connector.read()
    logging.info(f"Data read from source: {data}")

    # 4. Process the data
    if data:
        validated_data = validation_processor.process(data)
        if validated_data:
            transformed_data = transformation_processor.process(validated_data)
            logging.info(f"Transformed data: {transformed_data}")

            # 5. Write the data to the destination
            postgres_sink.write(transformed_data)
            logging.info("Data written to destination")
        else:
            logging.warning("Data validation failed, skipping transformation and sink")
    else:
        logging.warning("No data read from source, pipeline stopped")

    # 6. Close the sink connection
    postgres_sink.close()
    
    logging.info("Kafka Streaming ETL Pipeline finished")

if __name__ == "__main__":
    main()