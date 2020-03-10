FROM python:3.8.5-slim

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY ./namespace1/webservice ./namespace1/webservice

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 namespace1.webservice.app:app
