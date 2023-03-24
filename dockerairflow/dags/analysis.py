
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
    'dbt_airflow_analysis',
    default_args=default_args,
    description='A simple dbt and Airflow analysis DAG',
    schedule_interval='@daily',
)


# Define dbt commands as bash commands
dbt_run = BashOperator(
    task_id='dbt_run',
    bash_command='cd /dbt_project/analysis && dbt run --profiles-dir .',
    dag=dag,
)

dbt_compile = BashOperator(
    task_id='dbt_compile',
    bash_command='cd /yt_demo/analysis && dbt compile --profiles-dir .',
    dag=dag,
)


# Set up dependencies between tasks
dbt_run >> dbt_compile