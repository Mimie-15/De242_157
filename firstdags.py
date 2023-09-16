from __future__ import annotations

from datetime import datetime, timedelta
from textwrap import dedent
from airflow import DAG

from airflow.operators.bash import BashOperator
with DAG(
    "first_dags",
    default_args={
        "depends_on_past": False,
        "email": ["Nichakan.phati@gmail.com"],
    },
    description="A simple tutorial DAG",
    schedule=None,
    start_date=datetime(2021, 1, 1),
    tags=["example"],
) as dag:
    t1 = BashOperator(
        task_id="print_date",
        bash_command="date",
        )

    t2 = BashOperator(
        task_id="print_date2",
        bash_command="date",
        )

    t1 >> t2