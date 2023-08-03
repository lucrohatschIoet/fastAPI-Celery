FROM python:3.10-slim-bullseye
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# if any problem with installed packages, move pip install requiremetns to the begining
RUN python -m pip install --upgrade pip
RUN pip install celery redis

# new code after development ...
COPY ./worker.py ./worker.py

# start worker
CMD ["celery", "-A", "worker", "worker", "--loglevel=info", "--concurrency=1", "-O", "fair", "-Q", "redis_queue"]


# docker build -f dockerfile.celery_worker -t tw_worker:latest .
# docker run -p8008:8008 --network="host" face_worker:latest
