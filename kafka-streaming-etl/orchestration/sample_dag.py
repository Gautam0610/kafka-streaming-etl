from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def sample_task():
    print("This is a sample Airflow task.")

with DAG(
    dag_id='sample_etl_dag',
    schedule_interval=None,
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=['etl'],
) as dag:
    task1 = PythonOperator(
        task_id='sample_task',
        python_callable=sample_task,
    )