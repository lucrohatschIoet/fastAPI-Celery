from celery import Celery
from worker import run_task
from celery.result import AsyncResult
# from case import addition

BROKER='redis://:123456@localhost:6377/0'
BACKEND='redis://:123456@localhost:6377/0'

celery = Celery("redis_queue", broker=BROKER, backend=BACKEND)


async def add_task(x, y):
    print("adding task")
    bg_task = run_task.delay(x=x, y=y)
    print(f"Task created {bg_task}")
    return {"task": bg_task.id}


async def task_status(task_id):
    task = AsyncResult(id=task_id, app=celery)

    if task.ready():
        return task.get()

    return None
