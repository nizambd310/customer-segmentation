from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

local_workflow = DAG(
    "LocalIngestionDag",
    schedule_interval="0 6 2 * *",
    start_date = datetime(2023, 1, 1)
)

with local_workflow:
    echo_something = BashOperator(
        task_id='echo_something',
        bash_command='echo "1st dag" '
    )

    echo_something

# from airflow.operators.dummy import DummyOperator
# from airflow.operators.bash import BashOperator
# # The DummyOperator is a task and does nothing   
# accurate = DummyOperator(
# task_id='accurate'
# )
# # The BashOperator is a task to execute a bash command
# commands = BashOperator(
# task_id='commands'
# bash_command='sleep 5'
# )