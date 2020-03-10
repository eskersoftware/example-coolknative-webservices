FROM python:3.8.5-slim

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY ./namespace1/readwebservice ./namespace1/readwebservice

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 namespace1.readwebservice.app:app
