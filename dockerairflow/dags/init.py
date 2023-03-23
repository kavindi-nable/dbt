# from airflow import DAG
# from airflow.operators.python import PythonOperator, BranchPythonOperator
# from airflow.operators.bash import BashOperator
# from airflow.operators.dummy_operator import DummyOperator
# from datetime import datetime


# default_args = {
#     'owner': 'airflow',
#     'depends_on_past': False,
#     'start_date': datetime(2023,1,1),
#     'retries': 0
# }


# with DAG('1_init_once_seed_data', default_args=default_args, schedule_interval='@once') as dag:
#     task_1 = BashOperator(
#         task_id='load_seed_data_once',
#         bash_command='cd /dbt_demo && dbt seed --profiles-dir .',
#         dag=dag
#     )

# task_1 

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
    'dbt_airflow_sample',
    default_args=default_args,
    description='A simple dbt and Airflow example DAG',
    schedule_interval='@once',
)

# Set environment variables for dbt
os.environ['DBT_PROFILES_DIR'] = 'C:/Users/kavindim/.dbt/profiles.yml'
os.environ['DBT_PROJECT_DIR'] = 'C:/Users/kavindim/Documents/LearnDBT/dbt_demo'

# Define dbt commands as bash commands
dbt_seed = BashOperator(
    task_id='dbt_seed',
    bash_command='cd /dbt_demo && dbt seed --profiles-dir .',
    dag=dag,
)

dbt_run = BashOperator(
    task_id='dbt_run',
    bash_command='dbt run',
    dag=dag,
)

# dbt_test = BashOperator(
#     task_id='dbt_test',
#     bash_command='dbt test',
#     dag=dag,
# )

# Define a Python function to update a Slack channel with DAG status
# def notify_slack():
#     slack_message = f'DAG execution complete: {dag.dag_id}'
#     # add code here to send the message to Slack

# notify_slack = PythonOperator(
#     task_id='notify_slack',
#     python_callable=notify_slack,
#     dag=dag,
# )

# Set up dependencies between tasks
dbt_seed
