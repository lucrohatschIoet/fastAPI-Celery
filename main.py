from fastapi import FastAPI
from client import add_task, task_status


app = FastAPI(name="fastapi_celery")


@app.get('/')
async def home(x: int, y: int):
    print(f"Start with {x} and {y}")
    result = await add_task(
        x=x, y=y
    )

    return result


@app.get('/{task_id}')
async def get_status(task_id):
    status = await task_status(task_id)
    print(status)
    return status
