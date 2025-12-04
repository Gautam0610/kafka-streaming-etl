import logging
from prometheus_client import start_http_server, Summary, Gauge

# Initialize logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define custom metrics
DATA_INGESTION_TIME = Summary('data_ingestion_processing_time', 'Time spent on data ingestion')
DATA_TRANSFORMATION_TIME = Summary('data_transformation_processing_time', 'Time spent on data transformation')
DATA_VALIDATION_TIME = Summary('data_validation_processing_time', 'Time spent on data validation')
DATA_SINK_TIME = Summary('data_sink_processing_time', 'Time spent on data sink')
TOTAL_RECORDS_PROCESSED = Gauge('total_records_processed', 'Total number of records processed')

def start_metrics_server(port=8000):
    """
    Starts a Prometheus HTTP server to expose metrics.
    """
    try:
        start_http_server(port)
        logging.info(f"Started Prometheus metrics server on port {port}")
    except Exception as e:
        logging.error(f"Failed to start Prometheus metrics server: {e}")

if __name__ == '__main__':
    start_metrics_server()