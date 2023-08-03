from celery import Celery
import pickle
from case import addition
from time import sleep

BROKER='redis://:123456@localhost:6377/0'
BACKEND='redis://:123456@localhost:6377/0'

worker = Celery(
    "redis_queue",
    broker=BROKER,
    backend=BACKEND
    )


@worker.task
def run_task(x, y):
    print("Excecuting task")
    sleep(20)
    raise Exception("Bad function")
    result = addition(x, y)
    print(f"Result: {result}")
    return result

