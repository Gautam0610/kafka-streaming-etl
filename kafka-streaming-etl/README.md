# Kafka Streaming ETL Pipeline

This project implements a streaming ETL pipeline using Kafka for real-time data processing.

## Overview

The pipeline consists of the following layers:

-   **Ingestion:** Connectors for various data sources (REST APIs, databases, file systems).
-   **Processing:** Data transformation, validation, enrichment, and deduplication using custom processors.
-   **Sink:** Writing data to multiple destinations (PostgreSQL, MongoDB, Elasticsearch, S3).

## Folder Structure

-   `schemas/`: Avro schemas for data types.
-   `transformers/`: Pluggable transformation functions.
-   `validators/`: Data quality rules.
-   `config/`: Connector configurations.
-   `connectors/`: Source connectors implementation.
-   `processors/`: Data processing logic.
-   `sinks/`: Destination sinks implementation.
-   `monitoring/`: Metrics exporters and alerting rules.
-   `orchestration/`: Airflow DAGs for batch jobs.
-   `testing/`: Data fixtures and pipeline validation tests.
-   `documentation/`: Data dictionary and lineage diagrams.

## Usage

Detailed instructions on how to set up and run the pipeline will be provided later.

## Docker

A Dockerfile is included for containerizing the application.