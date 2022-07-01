from os import waitid
from threading import local
from airflow import DAG

from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator 

local_workflow = DAG(
    "LocalIngestionDAG", 
    schedule_interval="0 6 2 * *"
)

with local_workflow:
    
    transform_task = BashOperator(
        task_id = 'wget',
        bash_command = 'echo "hello world"'
    )
    ingest_task = BashOperator(
        task_id = 'ingest',
        bash_command = 'echo "hello world"'
    )


    transform_task >> ingest_task