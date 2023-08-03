# from worker import worker
# from celery import shared_task


# @worker.task(bind=True, name='addition')
def addition(x,y):
    return x + y
