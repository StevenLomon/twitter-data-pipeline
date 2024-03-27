import datetime, redis

from airflow import DAG
from airflow.operators.empty import EmptyOperator

my_dag = DAG(
    dag_id="my_dag_name",
    start_date=datetime.datetime(2024, 1, 1),
    schedule="@daily"
)
 
EmptyOperator(task_id="task")

r = redis.Redis(
  host='redis-18175.c327.europe-west1-2.gce.cloud.redislabs.com',
  port=18175,
  password='tfIixO8DhVjcWCDVjg3gBjuy3gYDyDZ7')

res1 = r.hset(
    "bike:1",
    mapping={
        "model": "Deimos",
        "brand": "Ergonom",
        "type": "Enduro bikes",
        "price": 4972,
    },
)

print(res1)

res2 = r.hget("bike:1", "model")
print(res2)

res3 = r.hget("bike:1", "price")
print(res3)

res4 = r.hgetall("bike:1")
print(res4)

print(r)