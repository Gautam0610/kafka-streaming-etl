# main.py
import logging

def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info("Starting Kafka Streaming ETL Pipeline")

    # TODO: Implement the pipeline logic here

    logging.info("Kafka Streaming ETL Pipeline finished")

if __name__ == "__main__":
    main()