
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import os

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'dbt_airflow_transform',
    default_args=default_args,
    description='A simple dbt and Airflow transformation DAG',
    schedule_interval='@daily',
)


# Define dbt commands as bash commands
dbt_run = BashOperator(
    task_id='dbt_run',
    bash_command='/dbt_project/transformation && dbt run --profiles-dir .',
    dag=dag,
)


# Set up dependencies between tasks
dbt_run