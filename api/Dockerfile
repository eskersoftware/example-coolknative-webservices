FROM python:3.8.5-slim

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY ./api ./api

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 api.entrypoints:app
