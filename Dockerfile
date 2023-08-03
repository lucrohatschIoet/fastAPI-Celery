FROM python:3.10-slim-bullseye
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install --upgrade pip wheel\
    && pip install -r requirements.txt
COPY ./case.py ./case.py
COPY ./main.py ./main.py
#ENTRYPOINT ["./scripts/run_server_prod.sh"]
CMD ['uvicorn' 'main:app' '--host' '0.0.0.0' '--port' '5000']
